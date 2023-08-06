from __future__ import absolute_import
import parmed
from .leapify import Leapify
from .utils import tempfolder, which, easy_call


class AmberBuilder(Leapify):
    ''' Require many programs in AmberTools (pytraj, tleap, nab, ...)

    Inheritance: AmberPDBFixer --> Leapify --> AmberBuilder
    '''

    def build_protein(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_protein
        self.parm = build_protein(*args, **kwargs)
        return self

    def build_bdna(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_bdna
        self.parm = build_bdna(*args, **kwargs)
        return self

    def build_adna(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_adna
        self.parm = build_adna(*args, **kwargs)
        return self

    def build_arna(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import build_arna
        self.parm = build_arna(*args, **kwargs)
        return self

    def solvate(self, *args, **kwargs):
        from pdb4amber.builder.pytraj_build import solvate
        self.parm = solvate(self.parm, *args, **kwargs)
        return self

    def build_unitcell(self):
        '''

        Requires
        --------
        UnitCell program (AmberTools)
        '''
        UnitCell = which('UnitCell')
        if self.parm.box is None or self.parm.symmetry is None:
            raise ValueError("Must have symmetry and box data")
        if not UnitCell:
            raise OSError("Can not find UnitCell program")

        with tempfolder():
            inp_pdb = 'inp.pdb'
            out_pdb = 'out.pdb'
            self.parm.save(inp_pdb)
            out = easy_call([
                UnitCell,
                '-p',
                inp_pdb,
                '-o',
                out_pdb,
            ])
            self.parm = parmed.load_file(out_pdb)

    def prop_pdb(self, irep):
        # TODO: change its name?
        ''' Use PropPDB to propagate a PDB structure.
        (EXPRERIMENTAL)
        
        Parameters
        ----------
        irep : Tuple[int]
            number of replicas along x, y, z axis.

        Requires
        --------
        PropPDB program (AmberTools)

        Examples
        --------
        >>> builder.prop_pdb((0, 1, 3))
        '''
        PropPDB = which('PropPDB')
        x, y, z = [str(i) for i in irep]
        if not PropPDB:
            raise OSError("Can not find UnitCell program")

        with tempfolder():
            inp_pdb = 'inp.pdb'
            out_pdb = 'out.pdb'
            self.parm.save(inp_pdb)
            out = easy_call([
                PropPDB,
                '-p',
                inp_pdb,
                '-ix',
                x,
                '-iy',
                y,
                '-iz',
                z,
                '-o',
                out_pdb,
            ])
            self.parm = parmed.load_file(out_pdb)
