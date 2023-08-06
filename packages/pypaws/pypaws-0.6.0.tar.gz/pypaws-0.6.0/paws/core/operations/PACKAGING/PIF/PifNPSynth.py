import numpy as np
import pypif.obj as pifobj

from ...Operation import Operation
from ... import optools

class PifNPSynth(Operation):
    """
    Package results from nanoparticle solution synthesis into a pypif.obj.ChemicalSystem object.
    """

    def __init__(self):
        input_names = ['uid_prefix','q_I','date_time','t_utc','T']
        output_names = ['pif']
        super(PifNPSynth,self).__init__(input_names,output_names)
        self.input_doc['uid_prefix'] = 'text string to prepend to pif uid (pif uid = uid_prefix+t_utc'
        self.input_doc['q_I'] = 'n-by-2 array of q values and corresponding intensities for saxs spectrum'
        self.input_doc['date_time'] = 'string date/time from measurement header file for pif record tags'
        self.input_doc['t_utc'] = 'time in seconds utc'
        self.input_doc['T'] = 'temperature in degrees celsius from measurement header file'
        self.output_doc['pif'] = 'pif object containing the relevant data for this experiment'
        self.input_src['uid_prefix'] = optools.text_input
        self.input_src['q_I'] = optools.wf_input
        self.input_src['date_time'] = optools.wf_input
        self.input_src['t_utc'] = optools.wf_input
        self.input_src['T'] = optools.wf_input
        self.input_type['uid_prefix'] = optools.str_type
        self.input_type['q_I'] = optools.ref_type
        self.input_type['date_time'] = optools.ref_type
        self.input_type['t_utc'] = optools.ref_type
        self.input_type['T'] = optools.ref_type

    def run(self):
        uid_pre = self.inputs['uid_prefix']
        t_str = self.inputs['date_time']
        t_utc = self.inputs['t_utc']
        uid_full = uid_pre+'_'+str(int(t_utc))
        T_C = self.inputs['T']
        q_I = self.inputs['q_I']
        # Subsystems for solution ingredients
        colloid_sys = pifobj.ChemicalSystem(uid_pre+'_pd_colloid',['colloidal Pd nanoparticles'],None,None,None,'Pd') 
        acid_sys = pifobj.ChemicalSystem(uid_pre+'_oleic_acid',['oleic acid'],None,None,None,'C18H34O2') 
        amine_sys = pifobj.ChemicalSystem(uid_pre+'_oleylamine',['oleylamine'],None,None,None,'C18H35NH2') 
        TOP_sys = pifobj.ChemicalSystem(uid_pre+'_trioctylphosphine',['trioctylphosphine'],None,None,None,'P(C8H17)3')
        subsys = [colloid_sys,acid_sys,amine_sys,TOP_sys]
        # TODO: Quantity information for subsystems
        main_sys = pifobj.ChemicalSystem()
        main_sys.uid = uid_full
        main_sys.sub_systems = subsys
        main_sys.properties = self.saxs_to_pif_properties(q_I,T_C)
        main_sys.tags = ['reaction id: '+uid_pre,'date: '+t_str,'utc: '+str(int(t_utc))]
        self.outputs['pif'] = main_sys

    def saxs_to_pif_properties(self,q_I,T_C):
        #props = []
        #for i in range(len(q)):
        pq = pifobj.Property()
        n_qpoints = q_I.shape[0]
        ### property: scattered intensity
        pI = pifobj.Property()
        pI.name = 'SAXS intensity'
        pI.scalars = [pifobj.Scalar(q_I[i,1]) for i in range(n_qpoints)]
        pI.units = 'counts'
        pI.conditions = []
        pI.conditions.append( pifobj.Value('SAXS scattering vector', 
                            [pifobj.Scalar(q_I[i,0]) for i in range(n_qpoints)],
                            None,None,'1/Angstrom') )
        pI.conditions.append(pifobj.Value('temperature',[pifobj.Scalar(T_C)],None,None,'degrees Celsius'))
        return [pq,pI] 
        
#    def make_piftemperature(self,t):
#        v = pifobj.Value()
#        v.name = 'temperature'
#        tscl = pifobj.Scalar()
#        tscl.value = str(t)
#        v.scalars = [tscl]
#        v.units = 'degrees Celsius'
#        return v
#
#    def make_pifvector(self,v):
#        pifv = []
#        for n in v:
#            s = pifobj.Scalar()
#            s.value = str(n)
#            pifv.append(s)
#        return pifv
#
#    def pifscalar(self,scl,errlo,errhi):
#        s = pifobj.Scalar()
#        s.value = str(scl) 
#        s.minimum = str(scl) 
#        s.maximum = str(scl) 
#        s.inclusiveMinimum = True
#        s.inclusiveMaximum = True
#        s.uncertainty = '+{},-{}'.format(errlo,errhi)
#        s.approximate = True
#        return s


