import numpy as np

from ...operation import Operation
from ... import optools

class NanoparticleFeatures(Operation):
    """
    Use a saxs spectrum (I(q) vs. q) to extract key features of a nanoparticle colloid:
    average size, standard deviation of sizes, and nanoparticle density.
    This module assumes spherical nanoparticles. 
    """

    def __init__(self):
        input_names = ['q','I','dI']
        output_names = ['ok_flag','mean_size','sigma_size','density','I_model']
        super(NanoparticleFeatures,self).__init__(input_names,output_names)        
        self.input_src['q'] = optools.wf_input
        self.input_src['I'] = optools.wf_input
        self.input_src['dI'] = optools.wf_input
        self.input_doc['q'] = '1d array specifying q values for a saxs spectrum'
        self.input_doc['I'] = '1d array specifying I(q)'
        self.input_doc['dI'] = '1d array specifying error in I(q)'
        self.output_doc['ok_flag'] = str('this flag is set to False if the spectrum '
        + 'does not resemble the sorts of spectra that this module expects to analyze. '
        + 'This module is written for dilute colloidal nanoparticle solutions.')
        self.output_doc['mean_size'] = 'average size of nanoparticles'
        self.output_doc['sigma_size'] = 'standard deviation of nanoparticle sizes'
        self.output_doc['density'] = 'density of nanoparticles'
        self.output_doc['I_model'] = str('the intensity spectrum '
        + 'found by fitting the input data to a model to perform feature extraction. '
        + 'The difference between I_model and the input I may indicate feature extraction quality.')
        
    def run(self):
        q = self.inputs['q']
        I = self.inputs['I']
        dI = self.inputs['dI']

        # If the maximum intensity is not somewhere up front, throw the flag
        if not np.argmax(I) in range(10):
            ok_flag = False
        else:
            ok_flag = True

        # Magnitude at zero: use the lowest-q value
        I_at_zero = I[0]

        # first minimum of I: walk until find point that is smallest within some window
        w = 10 
        found = False
        i = w
        while not found:
            if np.argmax(I[i-w:i+w+1]) == w:
                found = True
                q_at_first_min = q[i]
                curv_at_first_min = ((I[i+w]-I[i])/(q[i+w]-q[i]) 
                                    - (I[i]-I[i-w])/(q[i]-q[i-w]))/((q[i+w]-q[i-w])/2)
            elif i+w >= len(q):
                found = True
                q_at_first_min = 0
                curv_at_first_min = 0
            else:
                i += 1

        # least-squares to refine parameters:
        ### ... ###
        ### ... ###

        # any post-processing to extract the key quantities:
        rho = I_at_zero 
        p = curv_at_first_min 
        s = float(1)/q_at_first_min 
    
        # save results
        self.outputs['density'] = rho
        self.outputs['polydispersity'] = p
        self.outputs['mean_size'] = s
        self.outputs['ok_flag'] = ok_flag 

    @staticmethod
    def polydisperse_saxs(q,r0,p):
        """
        Generate spherical nanoparticle saxs spectrum for mean particle radius r0,
        size polydispersity (sigma(r)/r0) p, and scattering vectors q.
        """
        p = float(p)
        # Generate mesh of nanoparticle sizes
        if p == 0:
            rmesh = np.array([r0])
        else:
            rmesh = np.arange(r0-5*p,r0+5*p,p/10)
        rmesh = np.array([r for r in rmesh if r > 0])
        Itot = np.zeros(len(q))
        for r in rmesh:
            gauss_wt = (p*np.sqrt(2*np.pi))**(-1) * np.exp(-0.5*((r-r0)/p)**2)
            Itot += gauss_wt * self.monodisperse_saxs(q,r)
        return Itot
    
    @staticmethod
    def monodisperse_saxs(q,r):
        """
        Generate spherical nanoparticle saxs spectrum
        for monodisperse particle radius r at scattering vectors q.
        """
        x = q * r
        return ((np.sin(x) - x*np.cos(x)) * x**(-3))**2


