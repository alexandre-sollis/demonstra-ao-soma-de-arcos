from multiprocessing.reduction import DupFd
from manimlib import *

class Demonstracao_soma_arcos(Scene):
    def construct(self):

        posicao = (
            [-2.8,-3,0],[-1.6,-0.6,0],
            [0,-1.25,0],[0,2.8,0],
            [-5.75,-0.84,0],[-2.4,-3,0],
            [-1.2,0.1,0],[0,-1.3,0],
            [0,2,0],[-4.1,0.15,0],
            [0,-1.2,0],[-2.8,-2.9,0],
            [0.3,-1.6,0],[-0.47,1.6,0],
            [-4.5,-0.4,0]
            )  
        inicio_linha = (
            [2.5,-2.5,0],[2.5,1,0],
            [-2.5,1,0],[-2.5,-2.5,0],
            [2.5,-2.5,0],[2.5,-2.5,0],
            [-0.2,2.2,0],[-2.5,1,0],
            [2.5,1,0],[0.2,-2.5,0],
            [-1,-2.5,0],[-6,-2.5,0],
            [-1,-2.5,0],[-3.7,2.2,0],
            [-6,1,0],[-6,1,0],
            [-6,2.2,0],[-6,1,0],
            [-6,2.2,0]
            )
        final_linha = (
            [2.5,1,0],[-2.5,1,0],
            [-2.5,-2.5,0],[2.5,-2.5,0],
            [-2.5,1,0],[-0.2,2.2,0],
            [2.5,2.2,0],[-0.2,2.2,0],
            [2.5,2.2,0],[0.2,2.2,0],
            [-1,1,0],[-1,-2.5,0],
            [-3.7,2.2,0],[-1,2.2,0],
            [-3.7,2.2,0],[-6,2.2,0],
            [-3.7,2.2,0],[-6,2.2,0],
            [-3.7,2.2,0]
            )

        l_1 = Line(inicio_linha[0],final_linha[0], stroke_width = 4)
        l_2 = Line(inicio_linha[1],final_linha[1], stroke_width = 4)
        l_3 = Line(inicio_linha[2],final_linha[2], stroke_width = 4)
        l_4 = Line(inicio_linha[3],final_linha[3], stroke_width = 4)
        l_5 = Line(inicio_linha[4],final_linha[4], stroke_width = 4)
        l_6 = Line(inicio_linha[5],final_linha[5], stroke_width = 4)
        l_7 = Line(inicio_linha[6],final_linha[6], stroke_width = 4)
        l_8 = Line(inicio_linha[7],final_linha[7], stroke_width = 4)
        l_9 = Line(inicio_linha[8],final_linha[8], stroke_width = 4)
        l_10 = DashedLine(inicio_linha[9],final_linha[9], stroke_width = 4, dash_length = 0.2, color = YELLOW)
        l_11 = Line(inicio_linha[10],final_linha[10], stroke_width = 4, color = "#6A5ACD")
        l_12 = Line(inicio_linha[11],final_linha[11], stroke_width = 4, color =BLUE_D)
        l_13 = Line(inicio_linha[12],final_linha[12], stroke_width = 4, color=ORANGE)
        l_14 = Line(inicio_linha[13],final_linha[13], stroke_width = 4, color=GREEN_SCREEN)
        l_15 = Line(inicio_linha[14],final_linha[14], stroke_width = 4, color=RED_D)
        l_16 = Line(inicio_linha[15],final_linha[15], stroke_width = 4)
        l_17 = Line(inicio_linha[16],final_linha[16], stroke_width = 4)  
        l_18 = Line(inicio_linha[17],final_linha[17], stroke_width = 4, color=PINK)
        l_19 = Line(inicio_linha[18],final_linha[18], stroke_width = 4, color=PURPLE)


        quadrado_1 = Rectangle(width = 0.4, height = 0.4)
        quadrado_1.set_x(2.3)
        quadrado_1.set_y(0.8)
    
        ponto_angulo_1 = Tex("\\dot", font_size = 60)
        ponto_angulo_1.set_x(2.3)
        ponto_angulo_1.set_y(0.8)

        lado_x = Tex("x").rotate(1.565)
        lado_x.next_to(l_4, 1.2 * DOWN)

        lado_y = Tex("y").rotate(1.565)
        lado_y.next_to(l_1, 1.2*RIGHT)

        diagonal_ab = Tex("1").rotate(1.565)
        diagonal_ab.set_x(-0.5)
        diagonal_ab.set_y(-1)

        quadrado_2 = Rectangle(width = 0.4, height = 0.4).rotate(0.51)
        quadrado_2.set_x(-0.29)
        quadrado_2.set_y(1.93)
    
        ponto_angulo_2 = Tex("\\dot", font_size = 60)
        ponto_angulo_2.set_x(-0.29)
        ponto_angulo_2.set_y(1.93)

        arco_ab = ArcBetweenPoints(
            start = np.array([2.47,-1.5,0]),
            end = np.array([1.6,-1.85,0]))

        quadrado_3 = Rectangle(width = 0.4, height = 0.4)
        quadrado_3.set_x(2.3)
        quadrado_3.set_y(2)
    
        ponto_angulo_3 = Tex("\\dot", font_size = 60)
        ponto_angulo_3.set_x(2.3)
        ponto_angulo_3.set_y(2)

        angulo_a = Tex("a").rotate(1.565)
        angulo_a.set_x(2.1)
        angulo_a.set_y(-0.7)

        angulo_b = Tex("b").rotate(1.565)
        angulo_b.set_x(1.2)
        angulo_b.set_y(-1.1)

        poly_ab = [
            (2.5,-2.5,0), 
            (2.5,1,0),   
            (-2.5,1,0)]  

        triangulo_ab = Polygon(
            * poly_ab, 
            fill_opacity = 0.5,
            color = WHITE, 
            fill_color=BLUE)

        grupo = VGroup(l_1,l_2,l_3,l_4,l_5,l_6,l_7,l_8,l_9,arco_ab, diagonal_ab, angulo_a, angulo_b, lado_x, lado_y,quadrado_1,ponto_angulo_1,quadrado_2,ponto_angulo_2,quadrado_3,ponto_angulo_3)
        grupo2 = VGroup(diagonal_ab.copy(), triangulo_ab, arco_ab.copy(), lado_y.copy(), quadrado_1.copy(),ponto_angulo_1.copy())

        angulo_ab = Tex("(","a","+","b",")").rotate(1.565)
        angulo_ab.set_x(5.2)
        angulo_ab.set_y(1.2)

        lado_x2 = Tex("x").rotate(1.565)
        lado_x2.set_x(3.5)
        lado_x2.set_y(2.9)
        
        self.play(
            ShowCreation(l_1))
        self.play(
            ShowCreation(l_2))
        self.play(
            ShowCreation(l_3))
        self.play(
            ShowCreation(l_4))

        self.play(
            FadeIn(quadrado_1),
            FadeIn(ponto_angulo_1))

        self.play(
            Write(lado_x),
            Write(lado_y))

        self.wait()

        self.play(
            ShowCreation(l_5))
        self.wait()

        self.play(
            Write(diagonal_ab))

        self.play(
            ShowCreation(arco_ab))
        self.wait()

        self.play(
            ShowCreation(l_6))
        
        self.play(
            ShowCreation(l_8))
        
        self.play(
            FadeIn(quadrado_2),
            FadeIn(ponto_angulo_2))

        self.play(
            ShowCreation(l_7),
            ShowCreation(l_9))
    
        self.play(
            FadeIn(quadrado_3),
            FadeIn(ponto_angulo_3))
        
        self.play(
            Write(angulo_b),
            Write(angulo_a))
        self.wait()
        
        self.play(
            FadeIn(triangulo_ab))
        self.wait()

        self.play(
            ApplyMethod(grupo.shift, 3.5 * LEFT),
            ApplyMethod(grupo2.shift,3.5 * RIGHT + 1.5 * UP),
            TransformFromCopy(angulo_a,angulo_ab[1]),
            TransformFromCopy(angulo_b,angulo_ab[3]),
            TransformFromCopy(lado_x,lado_x2),
            Write(angulo_ab[0:8:2]))
        self.wait()

        sin_ab = Tex("sin","(a+b)", "=", "\\frac{\quad}{\quad}").rotate(1.565)
        sin_ab.set_x(1)
        sin_ab.set_y(-1.5)

        self.play(
            Write(sin_ab))

        self.play(
            lado_x2.copy().shift, 
            posicao[0],
            path_arc = 180 * DEGREES)

        diagonal_ab2 = Tex("1").rotate(1.565)
        diagonal_ab2.set_x(3)
        diagonal_ab2.set_y(0.5)

        self.play(
            diagonal_ab2.copy().shift,posicao[1])

        retangulo1 = Rectangle(width = 1.3, height = 0.8, color = BLACK , fill_opacity = 1)
        retangulo1.set_x(1)
        retangulo1.set_y(-0.1)

        lado_x3 = Tex("x").rotate(1.565)
        lado_x3.set_x(0.7)
        lado_x3.set_y(-0.1)

       
        self.play(FadeIn(retangulo1),
            lado_x3.shift,0.3 * RIGHT)
        self.wait()
        self.play(
            lado_x3.shift,posicao[2],
            sin_ab[0:2].shift,posicao[3],
            path_arc = 180 * DEGREES)
        self.wait()

        sin_ab2 = Tex("sin","(a+b)", "=", "\\frac{}{}",color = BLUE_D).rotate(3.131)
        sin_ab2.next_to(l_4, 1.2 * DOWN)

        self.play(
            Transform(sin_ab[0:2],sin_ab2[0:2]),
            FadeOut(lado_x),
            FadeOut(sin_ab[2]),
            FadeOut(lado_x3),
            ShowCreation(l_12))
        self.wait()

        lado_y2 = Tex("y").rotate(1.565)
        lado_y2.set_x(6.45)
        lado_y2.set_y(0.75)

        cos_ab = Tex("cos","(a+b)", "=", "\\frac{\quad}{\quad}").rotate(1.565)
        cos_ab.set_x(1)
        cos_ab.set_y(-1.5)
        self.play(Write(cos_ab))
        self.play(
            lado_y2.copy().shift, 
            posicao[4],
            path_arc = 180 * DEGREES)
        self.play(
            diagonal_ab2.copy().shift,
            posicao[1])

        lado_y3 = Tex("y").rotate(1.565)
        lado_y3.set_x(0.7)
        lado_y3.set_y(-0.09)

        self.play(FadeIn(retangulo1.copy()),
            lado_y3.shift,0.3 * RIGHT)
        self.wait()
        self.play(lado_y3.shift,posicao[2],cos_ab[0:2].shift,posicao[3],
            path_arc = 180 * DEGREES)
        self.wait()

        cos_ab2 = Tex("cos","(a+b)", "=", "\\frac{}{}",color = "#6A5ACD").rotate(1.565)
        cos_ab2.next_to(l_1, 1.2*RIGHT)

        self.play(
            Transform(cos_ab[0:2],cos_ab2[0:2]),
            FadeOut(lado_y),
            FadeOut(cos_ab[2]),
            FadeOut(lado_y3),
            ShowCreation(l_11))
        self.wait()

        retangulo2 = Rectangle(width = 7, height = 6, color = BLACK, fill_opacity = 1)
        retangulo2.set_x(4)
        retangulo2.set_y(1)
        self.play(FadeIn(retangulo2))

     #fecha o triangulo 1

        arco_b = ArcBetweenPoints(
            start=np.array([-1.58,-1.5,0]),
            end=np.array([-1.9,-1.8,0]))
        
        poly_b = [
            (-1,-2.5,0), 
            (-3.7,2.2,0),    
            (-6,1,0)]   
        triangulo_b = Polygon(
            * poly_b, 
            fill_opacity = 0.5, color = WHITE, fill_color = RED) 
            
        poly_b2 = [
            (5.5,-2.92,0), 
            (5.5,2.5,0),    
            (2.9,2.5,0)     
            ]

        triangulo_b2 = Polygon(
            * poly_b2, 
            fill_opacity = 0.5, color = WHITE, fill_color = RED)
        
        arco_b2 = ArcBetweenPoints(
            start = np.array([5.5,-1.45,0]),
            end = np.array([4.85,-1.55,0]))
     
        self.play(
            FadeIn(triangulo_b),
            run_time = 2)
        self.wait()
        diagonal_b2 = Tex("1").rotate(1.565)
        diagonal_b2.set_x(3.65)
        diagonal_b2.set_y(-0.21)

        angulo_b2 = Tex("b").rotate(1.565)
        angulo_b2.set_x(5)
        angulo_b2.set_y(-0.9)

        quadrado_2_2 = Rectangle(width = 0.4, height = 0.4)
        quadrado_2_2.set_x(5.3)
        quadrado_2_2.set_y(2.3)

        ponto_angulo_2_2 = Tex("\\dot", font_size = 60)
        ponto_angulo_2_2.set_x(5.3)
        ponto_angulo_2_2.set_y(2.3)

        grupo3 = VGroup(triangulo_b, diagonal_ab.copy(),angulo_b.copy(),arco_b, quadrado_2.copy(), ponto_angulo_2.copy())
        grupo4 = VGroup(triangulo_b2,diagonal_b2,angulo_b2,arco_b2, quadrado_2_2,ponto_angulo_2_2)

        self.play(Transform(grupo3,grupo4))
        self.wait()

        lado_m = Tex("m").rotate(1.565)
        lado_m.set_x(4.2)
        lado_m.set_y(2.9)

        lado_n = Tex("n").rotate(1.565)
        lado_n.set_x(5.9)
        lado_n.set_y(-0.21)

        self.play(
            Write(lado_m),
            Write(lado_n))
        
        self.wait()

        sin_b = Tex("sin","(b)", "=", "\\frac{\quad}{\quad}").rotate(1.565)
        sin_b.set_x(2.1)
        sin_b.set_y(-1.1)
        self.play(Write(sin_b))

        self.play(
            lado_m.copy().shift, 
            posicao[5],
            path_arc = 180 * DEGREES)

        self.play(
            diagonal_b2.copy().shift, 
            posicao[6])

        retangulo4 = Rectangle(width = 1.3, height = 0.8, color = BLACK, fill_opacity = 1)
        retangulo4.set_x(2)
        retangulo4.set_y(0)

        lado_m2 = Tex("m").rotate(1.565)
        lado_m2.set_x(1.8)
        lado_m2.set_y(-0.1)

        self.play(FadeIn(retangulo4),ApplyMethod(lado_m2.shift, 0.3 * RIGHT))
        self.wait()

        cos_b2 = Tex("cos","(b)", "\\frac{}{}", color = ORANGE, font_size = 40).rotate(2.15)
        cos_b2.set_x(-2.45)
        cos_b2.set_y(0.1)

        self.play(
            lado_m2.shift,posicao[7],
            sin_b[0:2].shift,posicao[8], 
            path_arc = 180 * DEGREES)
        self.wait()

        sin_b2 = Tex("sin","(b)", "=", "\\frac{\quad}{\quad}", color = RED_D, font_size = 35).rotate(3.65)
        sin_b2.set_x(-4.9)
        sin_b2.set_y(1.3)

        self.play(
            Transform(sin_b[0:2],sin_b2[0:2]),
            FadeOut(lado_m2),
            FadeOut(sin_b[2]),
            ShowCreation(l_15))
        self.wait()

        cos_b = Tex("cos","(b)", "=", "\\frac{\quad}{\quad}").rotate(1.565)
        cos_b.set_x(2.1)
        cos_b.set_y(-1.1)
        self.play(Write(cos_b))

        self.play(
            lado_n.copy().shift, 
            posicao[9],
            path_arc = 180 * DEGREES)

        self.play(
            diagonal_b2.copy().shift, 
            posicao[6])

        retangulo4 = Rectangle(width = 1.3, height = 0.8, color = BLACK, fill_opacity = 1)
        retangulo4.set_x(2)
        retangulo4.set_y(0)

        lado_n2 = Tex("n").rotate(1.565)
        lado_n2.set_x(1.8)
        lado_n2.set_y(-0.055)

        self.play(FadeIn(retangulo4),ApplyMethod(lado_n2.shift, 0.3 * RIGHT + 0.15 * DOWN))
        self.wait()

        self.play(
            lado_n2.shift,posicao[10],
            cos_b[0:2].shift,posicao[8],
            path_arc = 180 * DEGREES)
        self.wait()

        cos_b2 = Tex("cos","(b)", "\\frac{}{}", color = ORANGE, font_size = 40).rotate(2.15)
        cos_b2.set_x(-3)
        cos_b2.set_y(0.1)

        self.play(
            Transform(cos_b[0:2],cos_b2[0:2]),
            FadeOut(lado_n2),
            FadeOut(cos_b[2]),
            ShowCreation(l_13))
       
        self.wait()

        retangulo5 = Rectangle(width = 4,height = 7, color = BLACK, fill_opacity = 1)
        retangulo5.set_x(4)
        retangulo5.set_y(0)
        self.play(FadeIn(retangulo5))
        self.wait()

        #fecha triangulo 2

        poly_b = [
            (-1,-2.5,0),  
            (-1,2.2,0),    
            (-3.7,2.2,0)]  
        poly_b2 = [
            (5.5,-2.2,0),  
            (5.5,2.5,0),  
            (2.8,2.5,0)]   

        triangulo_b = Polygon(
            * poly_b,
            fill_opacity = 0.5,
            color = WHITE, 
            fill_color = GREEN)
        triangulo_b2 = Polygon(
            * poly_b2, 
            fill_opacity = 0.5, 
            color = WHITE, 
            fill_color = GREEN)
        
        self.play(
            FadeIn(triangulo_b),
            run_time = 2)
        self.wait()

        arco_b = ArcBetweenPoints(
            start = np.array([-1.03,-1.52,0]),
            end = np.array([-1.68,-1.6,0]))

        arco_b2 = ArcBetweenPoints(
            start = np.array([5.5,-0.8,0]),
            end = np.array([4.75,-0.9,0]))

        angulo_a2 = Tex("a").rotate(1.565)
        angulo_a2.set_x(5)
        angulo_a2.set_y(-0.2)

        diagonal_b = Tex("cos","(b)", "\\frac{}{}", font_size = 40).rotate(2.15)
        diagonal_b.set_x(3.55)
        diagonal_b.set_y(0.4)

        quadrado_3_3 = Rectangle(width = 0.4, height = 0.4)
        quadrado_3_3.set_x(5.3)
        quadrado_3_3.set_y(2.3)

        ponto_angulo_3_3 = Tex("\\dot", font_size = 60)
        ponto_angulo_3_3.set_x(5.3)
        ponto_angulo_3_3.set_y(2.3)


        grupo5 = VGroup(triangulo_b,angulo_a.copy(),arco_b.copy(),cos_b2, quadrado_3.copy(), ponto_angulo_3.copy())
        grupo6 = VGroup(triangulo_b2,angulo_a2,arco_b2,diagonal_b, quadrado_3_3, ponto_angulo_3_3)

        self.play(Transform(grupo5,grupo6))

        self.wait()

        lado_s = Tex("s").rotate(1.565)
        lado_s.set_x(5.9)
        lado_s.set_y(0.4)

        lado_r = Tex("r").rotate(1.565)
        lado_r.set_x(4.2)
        lado_r.set_y(2.9)

        self.play(
            Write(lado_r),
            Write(lado_s),
            run_time = 2)
        
        self.wait()

        sin_a = Tex("sin","(a)", "=", "\\frac{\quad}{\quad \, \quad \, \, \,}").rotate(1.565)
        sin_a.set_x(1.7)
        sin_a.set_y(-1.1)
        self.play(Write(sin_a))

        self.play(
            lado_r.copy().shift, 
            posicao[11],
            path_arc = 180 * DEGREES)

        diagonal_b2 = Tex("cos","(b)", "\\frac{}{}").rotate(1.565)
        diagonal_b2.set_x(2.15)
        diagonal_b2.set_y(-0.1)

        self.play(Transform(diagonal_b.copy(),diagonal_b2))
        self.wait()

        ponto_1 = SmallDot()
        ponto_1.set_x(1.72)
        ponto_1.set_y(0.7)

        lado_r2 = Tex("r").rotate(1.565)
        lado_r2.set_x(1.4)
        lado_r2.set_y(0)

        lado_s2 = Tex("s").rotate(1.565)
        lado_s2.set_x(1.4)
        lado_s2.set_y(0)

        retangulo6 = Rectangle(width = 1.8, height = 1.5, color = BLACK, fill_opacity = 1)
        retangulo6.set_x(2.1)
        retangulo6.set_y(-0.1) 

        self.play(FadeIn(retangulo6),lado_r2.shift, posicao[12],
            sin_a[0:2].shift,posicao[8],
            diagonal_b2.shift,posicao[13],
            path_arc = 180 * DEGREES)
        self.play(Write(ponto_1))

        sin_a_cos_b = Tex("sin","(a)", "\, \, \,", "cos","(b)", color = GREEN_SCREEN, font_size = 40).rotate(3.131)
        sin_a_cos_b.next_to(l_7, 1.2 * UP)
        ponto_2 = Tex("\dot", color = GREEN_SCREEN, font_size = 60)
        ponto_2.set_x(-2.35)
        ponto_2.set_y(2.7)
        self.wait()

        grupo7 = VGroup(sin_a[0:2],diagonal_b2[0:2],ponto_1)
        grupo8 = VGroup(sin_a_cos_b[0:2],sin_a_cos_b[2:4],ponto_2)

        self.play(
            Transform(grupo7,grupo8),
            FadeOut(lado_r2),
            FadeOut(sin_a[2]),
            ShowCreation(l_14))
        self.wait()

        retanguloa = Rectangle(width = 5,height = 6, color = BLACK, fill_opacity = 1)
        retanguloa.set_x(4)
        retanguloa.set_y(0) 

        cos_a = Tex("cos","(a)", "=", "\\frac{\quad}{\quad \, \quad \, \, \,}").rotate(1.565)
        cos_a.set_x(1.7)
        cos_a.set_y(-1.1)
        self.play(Write(cos_a))

        diagonal_b3 = Tex("cos","(b)", "\\frac{}{}").rotate(1.565)
        diagonal_b3.set_x(2.15)
        diagonal_b3.set_y(-0.1)

        self.play(
            lado_s.copy().shift, 
            posicao[14],
            path_arc = 180 * DEGREES)
        
        ponto_3 = SmallDot()
        ponto_3.set_x(1.72)
        ponto_3.set_y(0.7)

        self.play(Transform(diagonal_b.copy(),diagonal_b3))
        self.wait()

        self.play(FadeIn(retangulo6.copy()),lado_s2.shift,posicao[12],
            cos_a[0:2].shift,posicao[8],
            diagonal_b3.shift,posicao[13],
            path_arc = 180 * DEGREES)
        self.play(Write(ponto_3))

        self.play(FadeOut(lado_s2),FadeOut(cos_a[2]))

        cos_a3 = Tex("cos","(a)", "\, \, \, \,", "cos","(b)", color = YELLOW, font_size = 40).rotate(1.565)
        cos_a3.next_to(l_10, 1.2 * RIGHT)
        ponto_4 = Tex("\dot", color = YELLOW, font_size = 60)
        ponto_4.set_x(0.7)
        ponto_4.set_y(-0.15)

        self.play(
            Transform(cos_a[0:2], cos_a3[0:2]),
            Transform(diagonal_b3, cos_a3[2:5]),
            Transform(ponto_3, ponto_4),
            Write(l_10))
        self.wait()

        self.play(FadeIn(retanguloa))

        #fecha o triangulo 3

        quadrado_4 = Rectangle(width = 0.3, height = 0.3)
        quadrado_4.set_x(-5.85)
        quadrado_4.set_y(2.04)

        ponto_angulo_4 = Tex("\\dot", font_size = 40)
        ponto_angulo_4.set_x(-5.85)
        ponto_angulo_4.set_y(2.04)

        self.wait()

        self.play(ShowCreation(l_16))
        self.play(ShowCreation(l_17))
        self.play(
            FadeIn(quadrado_4),
            FadeIn(ponto_angulo_4))

        self.wait()

        arco_x = ArcBetweenPoints(
            start = np.array([-4.6,2.18,0]),
            end = np.array([-4.5,1.8,0]))

        self.play(
            ShowCreation(arco_x))
        self.wait()

        angulo_x = Tex("a", font_size = 40).rotate(3.131)
        angulo_x.set_x(-5)
        angulo_x.set_y(1.9)

        self.play(Transform(angulo_a.copy(), angulo_x))

        #até aqui tudo bem

        poly_x = [
            (-6,1,0),     
            (-6,2.2,0),    
            (-3.7,2.2,0)]  

        triangulo_x = Polygon(
            * poly_x, 
            fill_opacity = 0.5,
            color = WHITE, 
            fill_color = GREY) 
        self.play(FadeIn(triangulo_x))

        poly_x2 = [
            (-6,1,0),      
            (-6,2.2,0),    
            (-3.7,2.2,0)]  

        triangulo_x2 = Polygon(
            * poly_x2, 
            fill_opacity = 0.5,
            color = WHITE, 
            fill_color = GREY).rotate(4.695)
        triangulo_x2.set_x(5)
        triangulo_x2.set_y(0)
        self.wait()

        diagonal_x = Tex("sin","(b)", "\\frac{}{}", font_size = 40).rotate(2.15)
        diagonal_x.set_x(4.6)
        diagonal_x.set_y(-0.1)

        quadrado_4_4 = Rectangle(width = 0.3, height = 0.3)
        quadrado_4_4.set_x(5.44)
        quadrado_4_4.set_y(0.99)

        ponto_angulo_4_4 = Tex("\\dot", font_size = 40)
        ponto_angulo_4_4.set_x(5.44)
        ponto_angulo_4_4.set_y(0.99)

        arco_x2 = ArcBetweenPoints(
            start = np.array([5.545,-0.38,0]),
            end = np.array([5.2,-0.4,0]))

        angulo_x2 = Tex("a", font_size = 40).rotate(1.565)
        angulo_x2.set_x(5.3)
        angulo_x2.set_y(0)

        self.play(
            Transform(triangulo_x,triangulo_x2),
            Transform(sin_b2[0:2].copy(),diagonal_x),
            Transform(quadrado_4.copy(),quadrado_4_4),
            Transform(ponto_angulo_4.copy(), ponto_angulo_4_4),
            Transform(arco_x.copy(), arco_x2),
            Transform(angulo_x.copy(), angulo_x2))

        lado_u = Tex("u").rotate(1.565)
        lado_u.set_x(4.9)
        lado_u.set_y(1.5)

        lado_v = Tex("v").rotate(1.565)
        lado_v.set_x(5.9)
        lado_v.set_y(0.2)

        self.play(
            Write(lado_u),
            Write(lado_v))

        sin_x = Tex("sin","(a)", "=", "\\frac{\quad}{\quad \, \quad \, \, \,}").rotate(1.565)
        sin_x.set_x(2.5)
        sin_x.set_y(-1.1)
        self.play(Write(sin_x))

        sin_x2 = Tex("sin","(b)", "=", "\\frac{\quad}{\quad \, \quad \, \, \,}").rotate(1.565)
        sin_x2.set_x(2.95)
        sin_x2.set_y(1)

        lado_u2 = Tex("u").rotate(1.565)
        lado_u2.set_x(2.2)
        lado_u2.set_y(0)
     
        self.play(Transform(lado_u.copy(),lado_u2,path_arc = 180 * DEGREES))
        self.play(Transform(diagonal_x.copy(),sin_x2[0:2]))

        self.wait()

        retangulo7 = Rectangle(width = 2.4, height = 1.5, color = BLACK, fill_opacity = 1)
        retangulo7.set_x(2.3)
        retangulo7.set_y(-0.1)

        self.play(FadeIn(retangulo7),lado_u2.shift,posicao[12],
            sin_x[0:2].shift,posicao[8],
            sin_x2[0:2].shift,posicao[13],
            path_arc = 180 * DEGREES)

        ponto_5 = SmallDot()
        ponto_5.set_x(2.5)
        ponto_5.set_y(0.78)
        self.play(Write(ponto_5))

        sin_x3 = Tex("sin","(a)", "\, \, \, \,", "sin","(b)", color = PINK, font_size = 30).rotate(1.565)
        sin_x3.next_to(l_16, 0.8 * LEFT)
        ponto_6 = Tex("\dot", color = PINK, font_size = 30)
        ponto_6.next_to(l_16, 1.2 * LEFT)

        self.play(
            Transform(sin_x[0:2], sin_x3[0:2]),
            Transform(sin_x2[0:2], sin_x3[2:5]),
            Transform(ponto_5, ponto_6),
            ShowCreation(l_18),
            FadeOut(lado_u2),
            FadeOut(sin_x[2]))
        self.wait()

        cos_x = Tex("cos","(a)", "=", "\\frac{\quad}{\quad \, \quad \, \, \,}").rotate(1.565)
        cos_x.set_x(2.5)
        cos_x.set_y(-1.1)
        self.play(Write(cos_x))

        cos_x2 = Tex("sin","(b)", "=", "\\frac{\quad}{\quad \, \quad \, \, \,}").rotate(1.565)
        cos_x2.set_x(2.95)
        cos_x2.set_y(1)

        lado_v2 = Tex("v").rotate(1.565)
        lado_v2.set_x(2.2)
        lado_v2.set_y(0)

        self.play(Transform(lado_v.copy(),lado_v2,path_arc = 180 * DEGREES))
        self.play(Transform(diagonal_x.copy(),cos_x2[0:2]))

        self.wait()

        self.play(FadeIn(retangulo7.copy()),lado_v2.shift,posicao[12],
            cos_x[0:2].shift,posicao[8],
            cos_x2[0:2].shift,posicao[13],
            path_arc = 180 * DEGREES)

        ponto_7 = SmallDot()
        ponto_7.set_x(2.5)
        ponto_7.set_y(0.78)
        self.play(Write(ponto_7))

        cos_a_sin_b = Tex("cos","(a)", "\, \, \,", "sin","(b)", color = PURPLE, font_size = 40).rotate(3.131)
        cos_a_sin_b.next_to(l_17, 1.2 * UP)
        ponto_8 = Tex("\dot", color=PURPLE, font_size=60)
        ponto_8.set_x(-4.85)
        ponto_8.set_y(2.7)
        self.wait()

        grupo9 = VGroup(cos_x[0:2],cos_x2[0:2],ponto_7)
        grupo10 = VGroup(cos_a_sin_b[0:2],cos_a_sin_b[2:4],ponto_8)

        self.play(
            Transform(grupo9,grupo10),
            FadeOut(lado_v2),
            FadeOut(cos_x[2]),
            ShowCreation(l_19))
        self.wait()

        retangulo8 = Rectangle(width = 2.4, height = 3.5, color = BLACK, fill_opacity = 1)
        retangulo8.set_x(5)
        retangulo8.set_y(0.2)

        self.play(FadeIn(retangulo8))
        self.wait()

        sin_ab2_a1 = Tex("sin","(a+b)", "=", "sin","(a)", "\, \,", "cos","(b)","+","sin","(b)", "\, \,", "cos","(a)", font_size=35).rotate(1.565)
        sin_ab2_a1.set_x(3)
        sin_ab2_a1.set_y(0)

        sin_ab2_a = Tex("sin","(a+b)", "=", "sin","(a)", "\, \,", "cos","(b)","+","sin","(b)", "\, \,", "cos","(a)", font_size=35, color=BLUE_D).rotate(1.565)
        sin_ab2_a.set_x(3)
        sin_ab2_a.set_y(0)

        sin_ab2_a_2 = Tex("sin","(a+b)", "=", "sin","(a)", "\, \,", "cos","(b)","+","sin","(b)", "\, \,", "cos","(a)", font_size=35, color=GREEN_SCREEN).rotate(1.565)
        sin_ab2_a_2.set_x(3)
        sin_ab2_a_2.set_y(0)

        sin_ab2_a_2_2 = Tex("sin","(a+b)", "=", "sin","(a)", "\, \,", "cos","(b)","+","sin","(b)", "\, \,", "cos","(a)", font_size=35, color=PURPLE).rotate(1.565)
        sin_ab2_a_2_2.set_x(3)
        sin_ab2_a_2_2.set_y(0)

        ponto_9 = Tex("\\dot", font_size = 35, color = GREEN_SCREEN)
        ponto_9.next_to(sin_ab2_a_2[4], 0.3 * UP)

        ponto_10 = Tex("\\dot", font_size = 35, color = PURPLE)
        ponto_10.next_to(sin_ab2_a_2_2[9], 0.3 * UP)

        self.play(Transform(sin_ab2.copy()[0:2], sin_ab2_a[0:2]))
        self.play(
            Write(sin_ab2_a1[2]))
        self.wait()
        self.play(
            Transform(sin_a_cos_b.copy()[0:2], sin_ab2_a_2[3:5]),
            Transform(sin_a_cos_b.copy()[2:4], sin_ab2_a_2[5:7]),
            Transform(ponto_2, ponto_9))
        self.play(
            Write(sin_ab2_a1[7]))
        self.wait()

        self.play(
            Transform(cos_a_sin_b.copy()[0:2], sin_ab2_a_2_2[8:10]),
            Transform(cos_a_sin_b.copy()[2:4], sin_ab2_a_2_2[10:12]),
            Transform(ponto_8, ponto_10))
        self.wait()
        
        cos_ab2_a1 = Tex("cos","(a+b)", "=", "cos","(a)", "\, \,", "cos","(b)","-","sin","(a)", "\, \,", "sin","(b)", font_size=35).rotate(1.565)
        cos_ab2_a1.next_to(sin_ab2_a, 3 * RIGHT)

        cos_ab2_a = Tex("cos","(a+b)", "=", "cos","(a)", "\, \,", "cos","(b)","-","sin","(a)", "\, \,", "sin","(b)", font_size=35, color="#6A5ACD").rotate(1.565)
        cos_ab2_a.next_to(sin_ab2_a, 3 * RIGHT)

        cos_ab2_a_2 = Tex("cos","(a+b)", "=", "cos","(a)", "\, \,", "cos","(b)","-","sin","(a)", "\, \,", "sin","(b)", font_size=35, color=YELLOW).rotate(1.565)
        cos_ab2_a_2.next_to(sin_ab2_a, 3 * RIGHT)

        cos_ab2_a_2_2 = Tex("cos","(a+b)", "=", "cos","(a)", "\, \,", "cos","(b)","-","sin","(a)", "\, \,", "sin","(b)", font_size=35, color=PINK).rotate(1.565)
        cos_ab2_a_2_2.next_to(sin_ab2_a, 3 * RIGHT)

        self.play(Transform(cos_ab2.copy()[0:2], cos_ab2_a[0:2]))
        self.play(
            Write(cos_ab2_a1[2]))
        self.wait()

        ponto_11 = Tex("\\dot", font_size = 35, color = YELLOW)
        ponto_11.next_to(cos_ab2_a_2[4], 0.3 * UP)

        ponto_12 = Tex("\\dot", font_size = 35, color = PINK)
        ponto_12.next_to(cos_ab2_a_2_2[9], 0.3*UP)

        self.play(
            Transform(cos_a3.copy()[0:2], cos_ab2_a_2[3:5]),
            Transform(cos_a3.copy()[2:4], cos_ab2_a_2[5:7]),
            Transform(ponto_4, ponto_11))
        self.play(
            Write(cos_ab2_a1[7]))
        self.wait()

        self.play(
            Transform(sin_x3.copy()[0:2], cos_ab2_a_2_2[8:10]),
            Transform(sin_x3.copy()[2:4], cos_ab2_a_2_2[10:12]),
            Transform(ponto_6, ponto_12))
        self.wait()

        self.play(
            FadeToColor(sin_ab2_a[0:2], color = WHITE),
            FadeToColor(sin_ab2_a_2[3:7], color = WHITE),
            FadeToColor(sin_ab2_a_2_2[8:12], color = WHITE),
            FadeToColor(cos_ab2_a[0:2], color = WHITE),
            FadeToColor(cos_ab2_a_2[3:7], color = WHITE),
            FadeToColor(cos_ab2_a_2_2[8:12], color = WHITE),
            FadeToColor(ponto_9, color = WHITE),
            FadeToColor(ponto_10, color = WHITE),
            FadeToColor(ponto_11, color = WHITE),
            FadeToColor(ponto_12, color = WHITE))

        self.wait(3) 

       


