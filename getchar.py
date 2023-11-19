import sys, select, os, msvcrt, time
  
# class for checking keyboard input
class Getchar:
    def __init__(self): #def 함수선언 _init_ 변수선언과 초기화 (self 매개변수)
        pass    #파이썬은 괄호가 없고 들여쓰기 필수
  
    def getch(self): 
        if os.name == 'nt':
            timeout = 0.1
            startTime = time.time()
            while(1):
                if msvcrt.kbhit():
                    if sys.version_info[0] >= 3:
                        return msvcrt.getch().decode()
                    else:
                        return msvcrt.getch()
                elif time.time() - startTime > timeout:
                    return ''

        tty.setraw(sys.stdin.fileno())
        rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
        if rlist:
            key = sys.stdin.read(1)
        else:
            key = ''

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key
