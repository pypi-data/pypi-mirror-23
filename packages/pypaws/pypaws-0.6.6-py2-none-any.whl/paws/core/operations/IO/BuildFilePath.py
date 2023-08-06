from ..Operation import Operation
from .. import optools

class BuildFilePath(Operation):
    """
    This operation helps to build file paths from workflow data.
    It takes a directory (full path), a filename, and an extension.
    The filename can optionally have a prefix or suffix inserted,
    to help with iteration of batches of files with similar names.
    """

    def __init__(self):
        input_names = ['dir_path','prefix','filename','suffix','ext']
        output_names = ['filepath']
        super(BuildFilePath, self).__init__(input_names, output_names)
        self.input_doc['dir_path'] = 'filesystem path pointing to the directory containing the file- a trailing slash is optional'
        self.input_doc['prefix'] = 'any text to prepend to filename (prefix comes after dir_path, before filename)'
        self.input_doc['filename'] = 'name of the file, excluding any path, extension, prefix, or suffix'
        self.input_doc['suffix'] = 'any text to append to filename (comes after filename, before ext)'
        self.input_doc['ext'] = 'extension for the file- the leading period is optional'
        self.input_src['dir_path'] = optools.fs_input
        self.input_src['prefix'] = optools.text_input
        self.input_src['filename'] = optools.wf_input
        self.input_src['suffix'] = optools.text_input
        self.input_src['ext'] = optools.text_input
        self.input_type['dir_path'] = optools.path_type
        self.input_type['prefix'] = optools.str_type
        self.input_type['filename'] = optools.ref_type
        self.input_type['suffix'] = optools.str_type
        self.input_type['ext'] = optools.str_type
        self.inputs['prefix'] = ''
        self.inputs['suffix'] = ''
        self.output_doc['filepath'] = 'filepath will be <path>/<prefix><filename><suffix>.<ext>' 

    # TODO: Use os.path instead of manually building the directory / 
    def run(self):
        ext = self.inputs['ext']
        if not ext[0] == '.':
            ext = '.'+ext
        p = self.inputs['dir_path']
        if not p[-1] == '/':
            p = p + '/'
        fn = self.inputs['filename']
        pf = self.inputs['prefix']
        sf = self.inputs['suffix']
        self.outputs['filepath'] = p + pf + fn + sf + ext

