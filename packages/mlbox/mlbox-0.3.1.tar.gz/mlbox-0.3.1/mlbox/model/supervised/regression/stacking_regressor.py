# coding: utf-8
# Author: Axel ARONIO DE ROMBLAY <axelderomblay@gmail.com>
# License: BSD 3 clause


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_predict
from copy import copy as make_copy
from .regressor import *
import time


class StackingRegressor():

    """A Stacking regressor is a regressor that uses the predictions of several first layer estimators (generated with a cross validation method)
    for a second layer estimator.


    Parameters
    ----------

    base_estimators : list
        List of estimators to fit in the first level using a cross validation.

    level_estimator : object, optional (default=LinearRegression())
        The estimator used in second and last level

    n_folds : int, optional (default=5)
        Number of folds used to generate the meta features for the training set

    copy : boolean, optional (default=False)
        If true, meta features are added to the original dataset

    random_state : None, int or RandomState (default=1)
        Pseudo-random number generator state used for shuffling. If None, use default numpy RNG for shuffling.

    verbose : boolean, optional (default=True)
        Verbose mode.
    """



    def __init__(self, base_estimators = [Regressor(strategy="XGBoost"),Regressor(strategy="RandomForest"),Regressor(strategy="ExtraTrees")], level_estimator = LinearRegression(), n_folds = 5, copy = False, random_state = 1, verbose = True):

        self.base_estimators = base_estimators
        if(type(base_estimators)!=list):
            raise ValueError("base_estimators must be a list")
        else:
            for i,est in enumerate(self.base_estimators):
                self.base_estimators[i] = make_copy(est)

        self.level_estimator = level_estimator

        self.n_folds = n_folds
        if(type(n_folds)!=int):
            raise ValueError("n_folds must be an integer")

        self.copy = copy
        if(type(copy)!=bool):
            raise ValueError("copy must be a boolean")

        self.random_state = random_state
        if((type(self.random_state)!=int)&(self.random_state!=None)):
            raise ValueError("random_state must be either None or an integer")

        self.verbose = verbose
        if(type(self.verbose)!=bool):
            raise ValueError("verbose must be a boolean")

        self.__fitOK = False
        self.__fittransformOK = False



    def get_params(self, deep = True):

        return {'level_estimator': self.level_estimator,
            'base_estimators' : self.base_estimators,
            'n_folds' : self.n_folds,
            'copy' : self.copy,
            'random_state' : self.random_state,
                'verbose' : self.verbose}

    def set_params(self,**params):

        self.__fitOK = False
        self.__fittransformOK = False

        for k,v in params.items():
            if k not in self.get_params():
                warnings.warn("Invalid parameter a for stacking_regressor StackingRegressor. Parameter IGNORED. Check the list of available parameters with `stacking_regressor.get_params().keys()`")
            else:
                setattr(self,k,v)


    def fit_transform(self, X, y):

        """Create meta-features for the training dataset.

        Parameters
        ----------
        X : DataFrame, shape = [n_samples, n_features]
            The training dataset.

        y : pandas series of shape = [n_samples, ]
            The target

        Returns
        -------
        X_transform : DataFrame, shape = [n_samples, n_features*int(copy)+n_metafeatures]
            Returns the transformed training dataset.

        """

        ### sanity checks
        if((type(X)!=pd.SparseDataFrame)&(type(X)!=pd.DataFrame)):
            raise ValueError("X must be a DataFrame")

        if(type(y)!=pd.core.series.Series):
            raise ValueError("y must be a Series")


        cv = KFold(n_splits = self.n_folds,shuffle=True,random_state=self.random_state)

        preds = pd.DataFrame([], index=y.index)

        if(self.verbose):
            print("")
            print("[=============================================================================] LAYER [===================================================================================]")
            print("")

        for c, reg in enumerate(self.base_estimators):

            if(self.verbose):
                print("> fitting estimator n°"+ str(c+1) + " : "+ str(reg.get_params())+" ...")
                print("")

            y_pred = cross_val_predict(estimator = reg, X = X, y = y, cv = cv)     #for each base estimator, we create the meta feature on train set
            preds["est"+str(c+1)] = y_pred

            reg.fit(X, y)  # and we refit the base estimator on entire train set

        layer = 1
        while(len(np.intersect1d(X.columns, ["layer"+str(layer)+"_"+s for s in preds.columns]))>0):
            layer = layer + 1
        preds.columns = ["layer"+str(layer)+"_"+s for s in preds.columns]            
            
        self.__fittransformOK = True

        if(self.copy==True):
            return pd.concat([X, preds], axis=1)   #we keep also the initial features

        else:
            return preds    #we keep only the meta features


    def transform(self, X_test):

        """Create meta-features for the test dataset.

        Parameters
        ----------
        X_test : DataFrame, shape = [n_samples_test, n_features]
            The test dataset.

        Returns
        -------
        X_test_transform : DataFrame, shape = [n_samples_test, n_features*int(copy)+n_metafeatures]
            Returns the transformed test dataset.

        """

        ### sanity checks
        if((type(X_test)!=pd.SparseDataFrame)&(type(X_test)!=pd.DataFrame)):
            raise ValueError("X_test must be a DataFrame")


        if(self.__fittransformOK):

            preds_test = pd.DataFrame([], index=X_test.index)

            for c, reg in enumerate(self.base_estimators):

                y_pred_test = reg.predict(X_test)   #for each base estimator, we predict the meta feature on test set
                preds_test["est"+str(c+1)] = y_pred_test

            layer = 1
            while(len(np.intersect1d(X_test.columns, ["layer"+str(layer)+"_"+s for s in preds_test.columns]))>0):
                layer = layer + 1
            preds_test.columns = ["layer"+str(layer)+"_"+s for s in preds_test.columns]     
                
            if(self.copy==True):
                return pd.concat([X_test, preds_test], axis=1)   #we keep also the initial features
            else:
                return preds_test     #we keep only the meta features

        else:
            raise ValueError("Call fit_transform before !")


    def fit(self, X, y):

        """Fit the first level estimators and the second level estimator on X.

        Parameters
        ----------

        X : DataFrame, shape (n_samples, n_features)
            Input data, where ``n_samples`` is the number of samples and
            ``n_features`` is the number of features.

        y : pandas series of shape = [n_samples, ]
            The target

        Returns
        -------
        self : object
            Returns self.
        """


        X = self.fit_transform(X, y)    #we fit the base estimators

        if(self.verbose):
            print("")
            print("[=========================================================================] PREDICTION LAYER [============================================================================]")
            print("")
            print("> fitting estimator : "+str(self.level_estimator.get_params())+" ...")
            print("")

        self.level_estimator.fit(X.values, y.values)     #we fit the second level estimator

        self.__fitOK = True

        return self


    def predict(self, X_test):

        """Predict regression target for X_test using the meta-features.


        Parameters
        ----------
        X_test : DataFrame of shape = [n_samples_test, n_features]
            The testing samples

        Returns
        -------
        y : array of shape = [n_samples_test]
            The predicted values.

        """

        if(self.__fitOK):

            X_test = self.transform(X_test)   # we predict the meta features on test set

            return self.level_estimator.predict(X_test)    #we predict the target using the meta features

        else:

            raise ValueError("Call fit before !")


