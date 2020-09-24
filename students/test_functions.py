import unittest
from IPython.display import Markdown ,display


def printmd(string):

    display(Markdown(string))

def print_fail():
    printmd('**<span style="color: red;">TEST FAILED</span>**')

# Print a test passed message
def print_pass():
    printmd('**<span style="color: green;">TEST PASSED</span>**')

class Tests(unittest.TestCase):

    def test_one_hot(self,one_hot_function):

        try:

            self.assertEqual([1,0,0],one_hot_function('red'))
            self.assertEqual([1,0,0],one_hot_function('yellow'))
            self.assertEqual([1,0,0],one_hot_function('green'))

        except self.failureException as e:

            print_fail()
            print("your function did not return the except one hot-lable")
            print('\n',+str(0))
            return

        print_ass()

    def red_as_green(self,musiclassfied_images):

        for im,predicted_labal,true_label in musiclassfied_images:

            if (true_label == [1,0,0]):

                try:
                    self.assertEqual(predicted_labal,[0,0,1])

                except slef.failureException as e:

                    print_fail()

                    print("Waring : A red light as classfied as green")

                    print('\n'+str(e))

                    return

    print_pass()                                  
