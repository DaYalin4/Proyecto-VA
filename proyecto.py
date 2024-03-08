import mediapipe as mp  
import cv2
import serial

# sirve para dibujar con las utilidades de mediapipe
mp_dibujo = mp.solutions.drawing_utils

# para inicializar la solucion de detección de manos
mp_manos = mp.solutions.hands

objeto_hands = mp_manos.Hands(static_image_mode = False, 
                              max_num_hands = 1,
                              min_detection_confidence = 0.5)

cap = cv2.VideoCapture(1)

ventana1 = "Detección de manos"
cv2.namedWindow(ventana1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana1, 720, 420)

try:
    puerto = serial.Serial("COM3", 9600, timeout=1)
except:
    print("No hubo conexión")

#Creamos una funcion para obtener las coordenadas de un landmark 
def coord(landmark_dedo):
    dedo = puntos.landmark[landmark_dedo]
    coor_dedoX, coor_dedoY = int(dedo.x * 640), int(dedo.y * 480)
    return coor_dedoX, coor_dedoY
#Creamos una funcion para comparar las coordenadas de X
def compararX(l1, l2):
    x1, _ = coord(l1)
    x2, _ = coord(l2)
    return 1 if x1 > x2 else 0
#Creamos una funcion para comparar las coordenadas de Y
def compararY(l1, l2):
    _,y1 = coord(l1)
    _,y2= coord(l2)
    return 1 if y1 < y2 else 0

letra=0
while True:
    ret, frame =  cap.read()
    RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = objeto_hands.process(RGBframe)
    alto, ancho, canales = frame.shape


    if resultados.multi_hand_landmarks:
        for puntos in resultados.multi_hand_landmarks:

            #Para letra A: 
            if compararX(4,5) + compararY(4,3) + compararY(6,8) + compararY(10,12) + compararY(14,16) + compararY(18,20)==6:
                letra=1
                cv2.putText(frame, f"A", (500, 100), cv2.FONT_ITALIC, 1.5, (0,0,255), thickness=2)
            #Para la E: 
            elif compararX(5,4) + compararY(6,8) +compararY(10,12) + compararY(14,16) + compararY(18,20) +compararY(6,4)==6:
                cv2.putText(frame, f"E", (500, 100), cv2.FONT_ITALIC, 1.5, (0,0,255), thickness=2)
                letra=2
            #Para la I:
            elif compararY(20,19)+ compararY(6,8) + compararY(10,12) +compararY(14,16) + compararX(5,4) + compararY(7,4) + compararY(11,4) + compararY(15,4) ==8:
                cv2.putText(frame, f"I", (500, 100), cv2.FONT_ITALIC, 1.5, (0,0,255), thickness=2)
                letra=3
            #Para la O:
            elif compararY(8,5) + compararY(12,5)+compararY(16,5)+compararY(20,5)+compararX(4,5)+compararX(8,5)+compararX(12,5)+compararX(16,5)+compararX(20,5)+ compararX(1,12)==9:
                cv2.putText(frame, f"O", (500, 100), cv2.FONT_ITALIC, 1.5, (0,0,255), thickness=2)
                letra=4
            #Para la U:
            elif compararY(19,20)+compararY(15,16)+ compararY(8,11)+compararY(12,7)+ compararX(5,4)==5:
                cv2.putText(frame, f"U", (500, 100), cv2.FONT_ITALIC, 1.5, (0,0,255), thickness=2)
                letra=5
            else: 
                letra=0
    try:
        puerto.write(f"{letra}\n".encode())
        print("Letra:", letra)
    except:
        print("No se pueden enviar los datos")

    
    cv2.imshow(ventana1, frame)
    salir = cv2.waitKey(1)
    if salir == 27:
        break

cap.release()
cv2.destroyAllWindows()
