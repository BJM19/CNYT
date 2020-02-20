import unittest,calculadora

class TestCases(unittest.TestCase):
    def test_deberiaSumarDosNumerosComplejos(self):
        a=(-5,2)
        b=(4,-2)
        self.assertEqual(calculadora.suma(a,b),(-1,0))
    def test_deberiaRestarDosNumerosComplejos(self):
        a=(-5,2)
        b=(4,-2)
        self.assertEqual(calculadora.resta(a,b),(-9,4))
    def test_deberiaMultiplicarDosNumerosComplejos(self):
        a=(2,2)
        b=(-2,2)
        self.assertEqual(calculadora.producto(a,b),(-8,0))
    def test_deberiaDividirDosNumerosComplejos(self):
        a=(2,2)
        b=(-2,2)
        self.assertEqual(calculadora.division(a,b),(0.0,-1.0))
    def test_deberiaDarElOpuestoDeUnNumeroComplejo(self):
        a=(-2,-2)
        self.assertEqual(calculadora.opuesto(a),(2,2))
    def test_deberiaDarElConjugadoDeUnNumeroComplejo(self):
        a=(-2,-2)
        self.assertEqual(calculadora.conjugado(a),(-2,2))
    
    def test_deberiaDarElModuloDeUnNumeroComplejo(self):
        a=(2,2)
        self.assertEqual(calculadora.modulo(a),(2.8284271247461903))
    def test_deberiaPasarPolarACartesiano(self):
        a=(2,2)
        self.assertEqual(calculadora.polaresACartesianas(a),(1.9987816540381915, 0.06979899340500194))
    def test_deberiaPasarCartesianasAPolares(self):
        a=(1.9987816540381915, 0.06979899340500194)
        self.assertEqual(calculadora.cartesianasAPolares(a),(0.03490658503988659, 2.0))
    def test_deberiaDevolverLaFase(self):
        a=(2,2)
        self.assertEqual(calculadora.fase(a),(0.7853981633974483))
    def test_deberiaSumarDosVectoresDeNumerosComplejos(self):
        a=([(2,2),(3,3)])
        b=([(2,2),(3,3)])
        self.assertEqual(calculadora.adicionDeVectoresComplejos(a,b),[(4, 4), (6, 6)])
    def test_deberiaDarElInversoDeUnVectorDeNumerosCompejos(self):
        a=([(2,2),(3,3)])
        self.assertEqual(calculadora.inverso(a),[(-2, -2), (-3, -3)])
    def test_deberiaMulplicarUnEscalarPorUnVectorNumerosComplejos(self):
        a=([(2,2),(3,3)])
        b=2
        self.assertEqual(calculadora.escalarVector(a,b),[(4, 4), (6, 6)])
    def test_deberiaRelizarLaSumaDeDosMatricesDeNumerosComplejos(self):
        a=([[(2,2),(3,3)],[(2,2),(3,3)]])
        b=([[(2,2),(3,3)],[(2,2),(3,3)]])
        self.assertEqual(calculadora.sumaDeMatrices(a,b),[[(4, 4), (6, 6)], [(4, 4), (6, 6)]])
    def test_deberiaDevolverLaInversaDeUnaMaatriz(self):
        a=([[(2,2),(3,3)],[(2,2),(3,3)]])
        self.assertEqual(calculadora.inversaMatriz(a),[[(-2, -2), (-3, -3)], [(-2, -2), (-3, -3)]])
    def test_deberiaRealizarElProductoEntreDosMatricesDeNumerosComplejos(self):
         a=([[(2,2),(3,3)],[(2,2),(3,3)]])
         b=3
         self.assertEqual(calculadora.multiplicacionEscalarMatrices(a,b),[[(6, 6), (9, 9)]])
    def test_deberiaRealizarElProductoInternoEntreDosVectoresDeNumerosComplejos(self):
        a=([(2,2),(3,3)])
        b=([(2,2),(3,3)])
        self.assertEqual(calculadora.productoInternoDeVectores(a,b),(0, 26))
    def test_deberiaRealizarLaTrnspuestaDeUnaMatrizDeNumerosComplejos(self):
        a=([[(2,2),(3,3)],[(2,2),(3,3)]])
        self.assertEqual(calculadora.traspuesta(a),[[(2, 2), (2, 2)], [(3, 3), (3, 3)]])
    def test_deberiaRealizarLaConjugadaDeUnaMatrizDeNumerosComplejos(self):
         a=([[(2,2),(3,3)],[(2,2),(3,3)]])
         self.assertEqual(calculadora.conjugadaMatriz(a),[[(2, -2), (3, -3)], [(2, -2), (3, -3)]])
    def test_deberiaRealizarLaAdjuntaDeUnaMatrizDeNumerosComplejos(self):
         a=([[(2,2),(3,3)],[(2,2),(3,3)]])
         self.assertEqual(calculadora.adjunta(a),[[(2, -2), (2, -2)], [(3, -3), (3, -3)]])
    def test_deberiaRealizarLaMultiplicacionDeDosMatricesDeNumerosComplejos(self):
         a=([[(2,2),(3,3)],[(2,2),(3,3)]])
         b=([[(2,2),(3,3)],[(2,2),(3,3)]])   
         self.assertEqual(calculadora.multiplicacionMatices(a,b),[[(0, 20), (0, 30)], [(0, 20), (0, 30)]])
    def test_deberiaRealizarElProductoTensorEntreDosVectoresDeNumerosComplejos(self):
        a=([(2,2),(3,3)])
        b=([(2,2),(3,3)])
        self.assertEqual(calculadora.tensorVector(a,b),[(0, 8), (0, 12), (0, 12), (0, 18)])
    def test_deberiaRealizarLaMultiplicacionDeDosMatricesDeNumerosComplejos(self):
        a=([[(2,2),(3,3)],[(2,2),(3,3)]])
        b=([[(2,2),(3,3)],[(2,2),(3,3)]])   
        self.assertEqual(calculadora.tensorMatrices(a,b),[[(0, 8), (0, 12), (0, 12), (0, 18)], [(0, 8), (0, 12), (0, 12), (0, 18)], [(0, 8), (0, 12), (0, 12), (0, 18)], [(0, 8), (0, 12), (0, 12), (0, 18)]])
    def test_deberiaComprobarSiUnaMatrizEsHerminitiana(self):
        a=([[(0,0),(1,0)],[(1,0),(0,0)]])
        self.assertEqual(calculadora.esUnaHermitiana(a),True)
    def test_deberiaComprobarSiUnaMatrizEsUnitaria(self):
        a=([[(0,0),(1,0)],[(1,0),(0,0)]])
        self.assertEqual(calculadora.esUnaUnitaria(a),True)
    def test_deberiaRealizarLaNormaDeUnaMatriz(self):
        a=([[(0,0),(1,0)],[(1,0),(0,0)]])
        self.assertEqual(calculadora.normaMatriz(a),1.41)
if __name__=="__main__":
    unittest.main()
