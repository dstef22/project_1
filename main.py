from calc_controller import *
'''
    Final Project 1: Calculator.
        From lab 03 I am creating a gui to use the basic formulas.
        I am adding the new formulas power, percentage, plus/minus, and factorial.
        I am adding formulas to approximate for sin, cos, and e.
        I am adding a function to backspace, one to go back to the previous number, and one to clear.
    
    Project author:
    Dallin Stefanidis
    dstefanidis@unomaha.edu
    https://github.com/dstef22
    
    Credit and disclaimer:
    Gui design inspiration came from John Elder in this video: 
    https://www.youtube.com/watch?v=H1FpwbavWIk&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=8
    
    Icons used were created by Yusuke Kamiyamane and taken from https://p.yusukekamiyamane.com/.
    These icons are available under a Creative Commons Attribution 3.0 License 
    https://creativecommons.org/licenses/by/3.0/.
    Yusuke Kamiyamane had no part in creating this project.
'''


def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
