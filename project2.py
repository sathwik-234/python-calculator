import tkinter as tk
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("461x355")
        self.input_var = tk.StringVar()
        self.entry = tk.Entry(self.window, textvariable=self.input_var, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', 'sin', 'cos',
            'tan', 'asin', 'acos', 'atan',
            'log', 'sqrt', '=','sqr','pow','pi' ,'!','History'
        ]
        
        self.history_file = 'history.txt'  # Name of the history text file
        
        self.create_buttons()
        
        self.window.mainloop()
    
    def create_buttons(self):
        row = 1
        col = 0
        
        for button_text in self.buttons:
            button = tk.Button(self.window, text=button_text, width=15, command=lambda text=button_text: self.update_input(text))
            button.grid(row=row, column=col,ipady=8)
            col += 1
            
            if col > 3:
                col = 0
                row += 1
    
    def update_input(self, text):
        current_input = self.input_var.get()
        
        if text == '=':
            try:
                result = eval(current_input)
                self.input_var.set(result)
                self.add_to_history(current_input, result)  # Add input and output to history
            except ZeroDivisionError:
                self.input_var.set("Error: Division by zero")
            except Exception as e:
                self.input_var.set("Error: " + str(e))
        elif text == 'C':
            self.input_var.set("")
        elif text in ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']:
            function = getattr(math, text)  # Get the corresponding math function
            try:
                angle = float(current_input)
                result = function(math.radians(angle))  # Convert angle to radians if necessary
                self.input_var.set(result)
                self.add_to_history(current_input, result)  # Add input and output to history
            except ValueError:
                self.input_var.set("Error: Invalid input")
        elif text == 'pow':
            self.input_var.set(current_input + '**')
        elif text == 'History':
            self.display_history()  # Display history in a separate window
        elif text == 'pi':
            result =  self.input_var.set("3.14")
        elif text == 'sqr':
            result = self.input_var.set(current_input+'**2')
        elif text == '!':
            fact = 1 
            i = eval(current_input)
            while(i != 1):
                fact = fact * i
                i -= 1
            result = self.input_var.set(str(fact))
        else:
            self.input_var.set(current_input + text)
        
    
    def add_to_history(self, input_expr, output_result):
        history_entry = f"{input_expr} = {output_result}\n"
        
        with open(self.history_file, 'a') as file:
            file.write(history_entry)
    
    def display_history(self):
        with open(self.history_file, 'r') as file:
            history = file.read()
        
        # Create a new window to display the history
        history_window = tk.Toplevel(self.window)
        history_window.title("History")
        
        history_label = tk.Label(history_window, text=history, justify="left")
        history_label.pack(padx=10, pady=10)
    
# Create an instance of the Calculator class
calculator = Calculator()
