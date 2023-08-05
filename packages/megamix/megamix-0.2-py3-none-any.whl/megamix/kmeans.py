# -*- coding: utf-8 -*-
#
#Created on Mon Apr 10 14:20:27 2017
#
#author: Elina Thibeau-Sutre
#

import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

def dist_matrix(points,means,points_normed=None,distances='euclidean'):
    
    if distances == 'euclidean':
        points_ = points
        means_ = means
    elif distances == 'cosine':
        if points_normed is None:
            points_ = points/ np.linalg.norm(points,axis=1)[:,np.newaxis]
        else:
            points_ = points_normed
        means_ = means / np.linalg.norm(means,axis=1)[:,np.newaxis]
        
    dist_matrix = euclidean_distances(points_,means_)

    return dist_matrix

class Kmeans():

    """
    Kmeans model.
    
    Parameters
    ----------
    
    n_components : int, defaults to 1.
        Number of clusters used.
    
    init : str, defaults to 'kmeans'.
        Method used in order to perform the initialization,
        must be in ['random','plus','AF_KMC'].

    Attributes
    ----------
    
    name : str
        The name of the method : 'Kmeans'
        
    means : array of floats (n_components,dim)
        Contains the computed means of the model.
    
    iter : int
        The number of iterations computed with the method fit()
    
    _is_initialized : bool
        Ensures that the model has been initialized before using other
        methods such as distortion() or predict_assignements().
    
    Raises
    ------
    ValueError : if the parameters are inconsistent, for example if the cluster number is negative, init_type is not in ['resp','mcw']...
    
    References
    ----------
    'Fast and Provably Good Seedings for k-Means', O. Bachem, M. Lucic, S. Hassani, A.Krause
    'Lloyd's algorithm <https://en.wikipedia.org/wiki/Lloyd's_algorithm>'_
    'The remarkable k-means++ <https://normaldeviate.wordpress.com/2012/09/30/the-remarkable-k-means/>'_
 
    """
    def __init__(self,n_components=1,init="plus",n_jobs=1):
        
        super(Kmeans, self).__init__()

        self.name = 'Kmeans'
        self.n_components = n_components
        self.init = init
        self.n_jobs = n_jobs
        
        self._is_initialized = False
        self.iter = 0
        
        self._check_parameters()

    def _check_parameters(self):
        
        if self.n_components < 1:
            raise ValueError("The number of components cannot be less than 1")
        else:
            self.n_components = int(self.n_components)
        
        if self.init not in ['random', 'plus', 'kmeans', 'AF_KMC']:
            raise ValueError("Invalid value for 'init': %s "
                             "'init' should be in "
                             "['random', 'plus', 'kmeans', 'AF_KMC']"
                             % self.init)
    
    def _step_E(self,points,points_normed=None):
        """
        This method assign a cluster number to each point by changing its last coordinate
        Ex : if P belongs to the first cluster, then P[-1] = 0.
        
        :param points: an array (n_points,dim)
        :return assignments: an array (n_components,dim)
        
        """
        n_points,_ = points.shape
        assignements = np.zeros((n_points,self.n_components))
        
        M = dist_matrix(points,self.means,points_normed)
        for i in range(n_points):
            index_min = np.argmin(M[i]) #the cluster number of the ith point is index_min
            if (isinstance(index_min,np.int64)):
                assignements[i][index_min] = 1
            else: #Happens when two points are equally distant from a cluster mean
                assignements[i][index_min[0]] = 1
                
        return assignements
        
    def _step_M(self,points,assignements):
        """
        This method computes the new position of each means by minimizing the distortion
        
        Parameters
        ----------
        points : an array (n_points,dim)
        assignements : an array (n_components,dim)
            an array containing the responsibilities of the clusters
            
        """
        n_points,dim = points.shape
        
        for i in range(self.n_components):
            assignements_i = assignements[:,i:i+1]
            n_set = np.sum(assignements_i)
            idx_set,_ = np.where(assignements_i==1)
            sets = points[idx_set]
            if n_set > 0:
                self.means[i] = np.asarray(np.sum(sets, axis=0)/n_set)
    
    def distortion(self,points,assignements,points_normed=None):
        """
        This method returns the distortion measurement at the end of the k_means.
        
        Parameters
        ----------
        points : an array (n_points,dim)
        assignements : an array (n_components,dim)
            an array containing the responsibilities of the clusters
        Returns
        -------
        distortion : (float)
        
        """
        
        if self._is_initialized:
            n_points,_ = points.shape
            distortion = 0
            for i in range(self.n_components):
                assignements_i = assignements[:,i:i+1]
                n_set = np.sum(assignements_i)
                idx_set,_ = np.where(assignements_i==1)
                sets = points[idx_set]
                if points_normed is not None:
                    sets_normed = points_normed[idx_set]
                else:
                    sets_normed = None
                if n_set != 0:
                    M = dist_matrix(sets,self.means[i].reshape(1,-1),sets_normed)
                    distortion += np.sum(M)
                
            return distortion

        else:
            raise Exception("The model is not initialized")

        
    def fit(self,points_data,points_test=None,n_iter_max=100,
            n_iter_fix=None,tol=0,distances='euclidean'):
        """The k-means algorithm
        
        Parameters
        ----------
        points_data : array (n_points,dim)
            A 2D array of points on which the model will be trained
            
        tol : float, defaults to 0
            The EM algorithm will stop when the difference between two steps 
            regarding the distortion is less or equal to tol.
            
        n_iter_max : int, defaults to 100
            number of iterations maximum that can be done
        
        Other Parameters
        ----------------
        points_test : array (n_points_bis,dim) | Optional
            A 2D array of points on which the model will be tested.
        
        n_iter_fix : int | Optional
            If not None, the algorithm will exactly do the number of iterations
            of n_iter_fix and stop.
            
        Returns
        -------
        None
        
        """
        from .initializations import initialization_random
        from .initializations import initialization_plus_plus
        from .initializations import initialization_AF_KMC
        
        n_points,dim = points_data.shape
        
        if distances == 'cosine':
            points_data_normed = points_data/np.linalg.norm(points_data,axis=1)[:,np.newaxis]
            if points_test is not None:
                points_test_normed = points_test/np.linalg.norm(points_test,axis=1)[:,np.newaxis]
        else:
            points_data_normed = None
            points_test_normed = None
        
        #K-means++ initialization
        if (self.init == "random"):
            means = initialization_random(self.n_components,points_data)
        elif (self.init == "plus"):
            means = initialization_plus_plus(self.n_components,points_data)
        elif (self.init == "AF_KMC"):
            means = initialization_AF_KMC(self.n_components,points_data)
        else:
            raise ValueError("Invalid value for 'initialization': %s "
                                 "'initialization' should be in "
                                 "['random', 'plus','AF_KMC']"
                                  % self.init)
        self.means = means
        self.iter = 0
        self._is_initialized = True
        
        test_exists = points_test is not None
        first_iter = True
        resume_iter = True
        
        dist_data, dist_test = 0,0
        
        #K-means beginning
        while resume_iter:
            
            assignements_data = self._step_E(points_data,points_data_normed)
            dist_data_pre = dist_data
            if test_exists:
                assignements_test = self._step_E(points_test,points_test_normed)
                dist_test_pre = dist_test
            
            self._step_M(points_data,assignements_data)
            dist_data = self.distortion(points_data,assignements_data,points_data_normed)
            if test_exists:
                dist_test = self.distortion(points_test,assignements_test,points_test_normed)
            
            # Computation of resume_iter
            if first_iter:
                first_iter = False
                
            elif n_iter_fix is not None:
                resume_iter = self.iter < n_iter_fix
                
            elif self.iter > n_iter_max:
                resume_iter = False
                
            else:
                if test_exists:
                    criterion = (dist_test_pre - dist_test)/len(points_test)
                else:
                    criterion = (dist_data_pre - dist_data)/n_points
                resume_iter = (criterion > tol)
                    
            self.iter+=1
            
            
    def predict_assignements(self,points):
        """
        This function return the hard assignements of points once the model is
        fitted.
        
        """
    
        if self._is_initialized:
            assignements = self._step_E(points)
            return assignements

        else:
            raise Exception("The model is not initialized")
