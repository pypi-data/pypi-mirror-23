from __future__ import print_function, unicode_literals

import mimetypes
import os


class RequirementsDetector(object):
    """ Takes raw requirements argument, and detects / discovers all the requirements files. """

    filenames = []

    def __init__(self, requirements_arg):
        self.filenames = []

        if not requirements_arg:
            self.autodetect_files()
        else:
            self.detect_files(requirements_arg)

    def get_filenames(self):
        """ Returns a list of all filenames detected as proper requirements files. """
        return self.filenames

    def detect_files(self, requirements_arg):
        for argument in requirements_arg:
            if self._is_valid_requirements_file(argument):
                self.filenames.append(argument)
            else:  # pragma: nocover
                print('Invalid requirements file: {}'.format(argument))

    def autodetect_files(self):
        """ Attempt to detect requirements files in the current working directory """
        if self._is_valid_requirements_file('requirements.txt'):
            self.filenames.append('requirements.txt')

        if self._is_valid_requirements_file('requirements.pip'):  # pragma: nocover
            self.filenames.append('requirements.pip')

        if os.path.isdir('requirements'):
            for filename in os.listdir('requirements'):
                file_path = os.path.join('requirements', filename)
                if self._is_valid_requirements_file(file_path):
                    self.filenames.append(file_path)

    @staticmethod
    def _is_valid_requirements_file(filename):
        extension_ok = filename.endswith('txt') or filename.endswith('pip')
        return extension_ok and os.path.isfile(filename) and mimetypes.guess_type(filename)[0] in ['text/plain', None]
