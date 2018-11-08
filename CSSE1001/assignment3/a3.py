"""
Assignment 3 - Queue
CSSE1001/7030
Semester 2, 2018
"""

import tkinter as tk
from tkinter import simpledialog
import time
import math
from operator import attrgetter
from breakout import GameApp

__author__ = "Weiting Yin 44623515"


class TextContent:
    """
    A class including all the text for the app
    """
    def __init__(self):
        """
        Construct a container containg all the needed text
        """
        self.title = {
            'head': 'Important',
            'body': "Individual assessment items must be solely your own work. While students are encouraged to have " +
                 "high-level conversations about the problems they are\n" +
                 "tyring to solve, you must not look at another " +
                 "student's code or copy from it. " +
                 "The university uses sophisticated anti-collusion measures to automatically\n"
                 "detect similarity between assignment submissions.",
        }
        self.headline = {
            'quick': {
                'head': 'Quick Questions',
                'body': '< 2 mins with a tutor',
            },
            'long': {
                'head': 'Long Questions',
                'body': '> 2 mins with a tutor',
            },
        }
        self.description = {
            'quick': {
                'head': 'Some examples of quick questions:',
                'body': [
                    u'\u2022 ' + ' Syntax errors',
                    u'\u2022 ' + ' Interpreting error output',
                    u'\u2022 ' + ' Assignment/MyPyTutor interpretation',
                    u'\u2022 ' + ' MyPyTutor submission issues',
                ]
            },
            'long': {
                'head': 'Some examples of long questions:',
                'body': [
                    u'\u2022 ' + ' Open ended questions',
                    u'\u2022 ' + ' How to start a problem',
                    u'\u2022 ' + ' How to improve code',
                    u'\u2022 ' + ' Debugging',
                    u'\u2022 ' + ' Assignment help',
                ]
            }
        }
        self.request = {
            'quick': 'Request Quick Help',
            'long': 'Request Long Help',
        }
        self.queue_table_captions = {
            '#': 2,
            'Name': 13,
            'Questions Asked': 15,
            'Time': 22,
        }
        self.queue_table_cell_width = [2, 13, 15, 22]


class Title(tk.Frame):
    """
    A class to display the tile of the app
    """
    def __init__(self, master):
        """
        Construct a new title showing basic description

        Parameter:
            master: master of this frame
        """
        super().__init__(master, bg='#fefbed')
        content = TextContent()

        title_head = self.title(self, content.title['head'], '#fefbed', '#C09853', ('Arial', 18, 'bold'))
        self.pack_title(title_head)

        title_body = self.title(self, content.title['body'], '#fefbed', None, None)
        self.pack_title(title_body)

    def title(self, master, content, background, foreground, font_style):
        """
        Generate the tile label

        Parameters:
            master: master of this label
            content : the content
            background : the background color of the title
            foreground : the foreground color of the title
            font_style : the font style of the title
        """
        title_widget = tk.Label(master, text=content, bg=background, anchor='w',
                                justify=tk.LEFT, fg=foreground, font=font_style)
        return title_widget

    def pack_title(self, title):
        """
        pack the title widget into the frame
        """
        title.pack(side=tk.TOP, fill=tk.X, padx=20, pady=10)


class HeadLineFrame(tk.Frame):
    """
    A class to generate outside frame for the headline
    """
    def frame(self):
        """
        Return the generated and packed frame
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=20, ipady=20)
        return frame


class HeadLine(HeadLineFrame):
    """
    A class to generate the headline
    """
    def __init__(self, master):
        """
        Construct a new headline

        Parameter:
            master: the master of this headline
        """
        super().__init__(master)
        content = TextContent()

        quick_frame = self.frame()
        long_frame = self.frame()

        quick_headline_head = self.headline(quick_frame, '#dff0d8', content.headline['quick']['head'],
                                            ('Arial', 30, 'bold'), '#3c763d')
        self.pack_headline(quick_headline_head)
        quick_headline_body = self.headline(quick_frame, '#dff0d8', content.headline['quick']['body'], None, None)
        self.pack_headline(quick_headline_body)

        long_headline_head = self.headline(long_frame, '#d9edf7', content.headline['long']['head'],
                                           ('Arial', 30, 'bold'), '#31708f')
        self.pack_headline(long_headline_head)
        long_headline_body = self.headline(long_frame, '#d9edf7', content.headline['long']['body'], None, None)
        self.pack_headline(long_headline_body)

    def headline(self, master, background, content, font_style, foreground):
        """
        Parameters:
            master: master of the headline
            background: background of the headline
            content: content of the headline
            font_style: font style of the headline
            foreground: foreground color of the headline

        Return:
            the headline widget
        """
        headline_widget = tk.Label(master, bg=background, text=content,
                                   font=font_style, fg=foreground)
        return headline_widget

    def pack_headline(self, headline):
        """
        Pack the headline widget

        Parameter:
            headline: the headline widget

        """
        headline.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


class DescriptionFrame(tk.Frame):
    """
    A class to generate the description frame
    """
    def frame(self):
        """
        Return:
              the outside frame of the description widget
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20)
        return frame


class Description(DescriptionFrame):
    """
    A class to generate description widget
    """
    def __init__(self, master):
        """
        Construct a new description widget

        Parameter:
            master: master of this widget
        """
        super().__init__(master)
        content = TextContent()

        quick_frame = self.frame()
        long_frame = self.frame()

        quick_desc_head = self.desc_head(quick_frame, content.description['quick']['head'])
        self.pack_desc_head(quick_desc_head)
        self.pack_desc_body(quick_frame, content.description['quick']['body'])

        # long part
        long_desc_head = self.desc_head(long_frame, content.description['long']['head'])
        self.pack_desc_head(long_desc_head)
        self.pack_desc_body(long_frame, content.description['long']['body'])

    def desc_head(self, master, content):
        """
        Generate the description head widget

        Parameters:
            master: master of thid widget
            content: content be displayed for this widget
        """
        description_head = tk.Label(master, text=content)
        return description_head

    def pack_desc_head(self, desc):
        """
        Pack the description widget

        Parameter:
            desc: the description widget
        """
        desc.pack(side=tk.TOP, anchor=tk.W)

    def pack_desc_body(self, master, contents: list):
        """
        Generate the description body widget

        Parameters:
            master: master of this widget
            contents (list): a list containing all the content needed to be displayed
        """
        for widget_text in contents:
            widget = tk.Label(master, text=widget_text)
            widget.pack(side=tk.TOP, anchor=tk.W, padx=20)


class RequestFrame(tk.Frame):
    """
    A class to generate request fame
    """
    def frame(self):
        """
        Return a packed request frame
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=5, ipady=10)
        return frame


class Request(RequestFrame):
    """
    A class to generate Request widget
    """
    def __init__(self, master):
        """
        Construct a new request widget

        Parameter:
            master: the master of this request widget
        """
        super().__init__(master)
        self._master = master
        content = TextContent()
        quick_frame = self.frame()
        long_frame = self.frame()

        self._quick_request_btn = self.request_button(quick_frame, content.request['quick'], '#5cb85c')
        self.pack_button(self._quick_request_btn)
        self._quick_request_btn.bind('<Button-1>', self.quick_callback)

        self._long_request_btn = self.request_button(long_frame, content.request['quick'], '#5bc0de')
        self.pack_button(self._long_request_btn)
        self._long_request_btn.bind('<Button-1>', self.long_callback)

    def request_button(self, master, content, background):
        """
        Generate th request button

        Parameters:
            master: master of this widget
            content: the content of this widget
            background: the background of the widget

        Return:
            the request button widget
        """
        request_btn = tk.Button(master, text=content, bg=background, fg='black')
        return request_btn

    def pack_button(self, button):
        """
        Pack the request button
        """
        button.pack(side=tk.TOP, expand=True, ipadx=5, ipady=5, pady=10)

    def dialog(self, title, master):
        """
        Generate a simple dialog to let user input their name

        Parameters:
            title: the title of the window
            master: the master of the widget

        Return:
            name (str): the input name
        """
        name = simpledialog.askstring(title, 'What is your name: ', parent=master)
        return name

    def quick_callback(self, event):
        """
        The action performed when the user click the quick request button.
        """
        name = self.dialog('quick request', self._quick_request_btn)
        quick_queue = app.get_quick_queue()
        long_queue = app.get_long_queue()
        quick_queue_records = app.get_quick_queue_records()
        # Determine if the student has already joined the queue
        if name is None:
            return
        if quick_queue.find_by_name(name) is not None:
            return
        if long_queue.find_by_name(name) is not None:
            return
        student = quick_queue_records.find_by_name(name)
        student_table = app.get_student_table()
        if student is None:
            # this means student have not asked a question before
            # create a new student
            student = Student(name, 'a few seconds ago')
            quick_queue_records.add_student(student)

        # add student, start track
        student.start_track()
        quick_queue.add_student(student)
        quick_queue.sort_queue()
        student_table.quick_repack_all()

    def long_callback(self, event):
        """
        The action performed when the user click the long request button.
        """
        name = self.dialog('long request', self._long_request_btn)
        quick_queue = app.get_quick_queue()
        long_queue = app.get_long_queue()
        long_queue_records = app.get_long_queue_records()
        # Determine if the student has already joined the queue
        if name is None:
            return
        if quick_queue.find_by_name(name) is not None:
            return
        if long_queue.find_by_name(name) is not None:
            return
        student = long_queue_records.find_by_name(name)
        student_table = app.get_student_table()
        if student is None:
            # this means student have not asked a question before, create a new student instead
            student = Student(name, 'a few seconds ago')
            long_queue_records.add_student(student)
        # add student, start track
        student.start_track()
        long_queue.add_student(student)
        long_queue.sort_queue()
        student_table.long_repack_all()


class Line(tk.Canvas):
    """
    A class to generate horizontal line
    """
    GAP = 5
    THICKNESS = 10
    LENGTH = 470

    def __init__(self, master):
        """
        Construct a new line
        """
        super().__init__(master, height=self.GAP)
        self.draw_line()
        self.pack_line()

    def draw_line(self):
        """
        Draw the line
        """
        self.create_line(0, 0, self.LENGTH, 0, fill='#eee', width=self.THICKNESS)

    def pack_line(self):
        """
        Pack the line
        """
        self.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


class QueueInfoFrame(tk.Frame):
    """
    A class to generate queue title frame
    """
    def frame(self):
        """
        Return:
            frame of the queue title
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=20, anchor=tk.W)
        return frame


class QueueInfo(QueueInfoFrame):
    """
    A class to generate queue title widget
    """
    def __init__(self, master):
        """
        Construct a new queue title widget, will display average waiting time

        Parameter:
            master: master of this widget
        """
        super().__init__(master)
        quick_frame = self.frame()
        long_frame = self.frame()

        Line(quick_frame)
        self._quick_info = self.info_label(quick_frame, 'No students in queue')
        self.pack_info_label(self._quick_info)
        Line(quick_frame)

        Line(long_frame)
        self._long_info = self.info_label(long_frame, 'No students in queue')
        self.pack_info_label(self._long_info)
        Line(long_frame)

    def info_label(self, master, content):
        """
        Generate a label for queue title to display avg waiting time

        Parameters:
            master: the master of the widget
            content: the content to be displayed
        """
        info_widget = tk.Label(master, text=content, anchor='w', justify=tk.LEFT)
        return info_widget

    def pack_info_label(self, queue_info):
        """
        Pack title information label

        Parameter:
            queue_info: the queue info label
        """
        queue_info.pack(side=tk.TOP, anchor=tk.W)

    def set_quick_info_content(self, content):
        """
        Modify the quick queue info label's content

        Parameter:
            content: the content need to be reset
        """
        self._quick_info.config(text=content)

    def set_long_info_content(self, content):
        """
        Modify the long queue info label's content

        Parameter:
            content: the content need to be reset
        """
        self._long_info.config(text=content)


class StudentTableCaptionFrame(tk.Frame):
    """
    A class to generate the student queue caption frame
    """
    def quick_frame(self):
        """
        Return the quick queue caption frame
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20)
        return frame

    def long_frame(self):
        """
        Return the long queue caption frame
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20)
        return frame

    def row_frame(self, master):
        """
        Return the row frame to contain all the caption cell label
        """
        frame = tk.Frame(master)
        frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        return frame


class StudentTableCaption(StudentTableCaptionFrame):
    """
    A class to generate student queue table caption
    """
    def __init__(self, master):
        """
        Construct a new student queue table caption

        Parameter:
            master: the master of this widget
        """
        super().__init__(master)
        content = TextContent()
        captions = content.queue_table_captions
        quick_frame = self.quick_frame()
        quick_row_frame = self.row_frame(quick_frame)
        long_frame = self.long_frame()
        long_row_frame = self.row_frame(long_frame)

        self.caption_row(quick_row_frame, captions)
        Line(quick_frame)

        self.caption_row(long_row_frame, captions)
        Line(long_frame)

    def caption_row(self, master, captions: dict):
        """
        Pack all the cell caption in to a caption frame

        Parameters:
            master: the master of this widget
            captions (dict): a dict containing displayed text and cell space for each cell
                            {'text': 5}
        """
        for caption, space in captions.items():
            cell = tk.Label(master, text=caption, anchor='w', justify=tk.LEFT, width=space)
            cell.pack(side=tk.LEFT, anchor=tk.W)


class StudentTableFrame(tk.Frame):
    """
    A class to generate student queue table frame
    """
    def quick_frame(self):
        """
        Return the quick student queue table frame
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.LEFT, anchor=tk.N, padx=20)
        return frame

    def long_frame(self):
        """
        Return the long student queue table frame
        """
        frame = tk.Frame(self)
        frame.pack(side=tk.RIGHT, anchor=tk.N, padx=10)
        return frame

    def row_frame(self, master):
        """
        Parameter:
            master: the master of the frame, would be either quick frame or long frame

        Return a frame row that could contain all the student information
        """
        frame = tk.Frame(master)
        frame.pack(side=tk.TOP)
        return frame


class StudentTable(StudentTableFrame):
    """
    A class to generate the student table
    """
    def __init__(self, master):
        """
        Construct a new student queue table
        """
        super().__init__(master)
        self._master = master
        content = TextContent()
        self._cell_width = content.queue_table_cell_width
        self._quick_frame = self.quick_frame()
        self._long_frame = self.long_frame()

    def button(self, master, color):
        """
        Return a packed button that will be append

        Parameter:
            color (str): the background color of the button
        """
        btn = tk.Button(master, width=2, bg=color)
        btn.pack(side=tk.LEFT, anchor=tk.W)
        return btn

    def add_student_row(self, master, student_info: list):
        """
        Add a student row into the student table

        Parameters
            master: mater of the row
            student_info (list): A list containing all the information that a student needed to displayed

        Return:
            this packed student row frame
        """
        row_frame = self.row_frame(master)
        id = len(list(master.children.values()))
        for index, cell_width in enumerate(self._cell_width):
            if index == 0:
                cell = tk.Label(row_frame, text=str(id), anchor='w', justify=tk.LEFT, width=cell_width)
            else:
                cell = tk.Label(row_frame, text=student_info[index-1], anchor='w', justify=tk.LEFT, width=cell_width)
            cell.pack(side=tk.LEFT, anchor=tk.W)

        btn_red = self.button(row_frame, '#F6A2A4')
        btn_green = self.button(row_frame, '#A0E3AE')

        if master == self._quick_frame:
            btn_red.bind('<Button-1>', self.quick_red_help)
            btn_green.bind('<Button-1>', self.quick_green_help)
        else:
            btn_red.bind('<Button-1>', self.long_red_help)
            btn_green.bind('<Button-1>', self.long_green_help)
        return row_frame

    def repack_all(self, master, queue):
        """
        Repack all the student row in the student table

        Parameters:
            master: master of the widget
            queue: relevant queue
        """
        # destroy all
        for row in list(master.children.values()):
            row.destroy()
        # repack
        students = queue.get_students()
        for student in students:
            quick_row_frame = self.add_student_row(master, student.info)
            # store relevant row widget
            student.store_widget(quick_row_frame)

    def quick_repack_all(self):
        """
        Repack all the row in the quick queue table
        """
        quick_queue = app.get_quick_queue()
        self.repack_all(self._quick_frame, quick_queue)

    def long_repack_all(self):
        """
        Repack all the row in the long queue table
        """
        long_queue = app.get_long_queue()
        self.repack_all(self._long_frame, long_queue)

    def red_help(self, queue, target):
        """
        Perform relative action when someone click the red button

        Parameters:
            queue: queue that needed to be used
            target: the target red button that trigger the event

        Return:
            the student instance that be removed from the queue
        """
        name_label = list(target.master.children.values())[1]
        name = name_label.cget('text')
        # destroy row
        # note: the label stored in student has also been detroyed
        target.master.destroy()
        # update label id
        self.update_id(target)
        # remove student
        removed_student = queue.remove_by_name(name)
        # clear track
        removed_student.clear_track()
        return removed_student

    def green_help(self, queue, target):
        """
        Perform relative action when someone click the green button
        the student's question asked attribute will be added one

        Parameters:
            queue: queue that needed to be used
            target: the target green button that trigger the event

        Return:
            the student instance that be removed from the queue
        """
        removed_student = self.red_help(queue, target)
        removed_student.increase_asked_ques()

    def quick_red_help(self, event):
        """
        Trigger the quick red help button event
        """
        quick_queue = app.get_quick_queue()
        target = event.widget
        self.red_help(quick_queue, target)

    def quick_green_help(self, event):
        """
        Trigger the quick green help button event
        """
        quick_queue = app.get_quick_queue()
        target = event.widget
        self.green_help(quick_queue, target)

    def long_red_help(self, event):
        """
        Trigger the long red help button event
        """
        long_queue = app.get_long_queue()
        target = event.widget
        self.red_help(long_queue, target)

    def long_green_help(self, event):
        """
        Trigger the long green help button event
        """
        long_queue = app.get_long_queue()
        target = event.widget
        self.green_help(long_queue, target)

    def update_id(self, target):
        """
        Update all the student's row's id in the student table

        Parameters:
            target: the target widget that trigger this action
        """
        target_frame = target.master.master
        rows = list(target_frame.children.values())
        for index, row in enumerate(rows):
            id_label = list(row.children.values())[0]
            id_label.config(text=str(index+1))


class Student:
    """
    A class to generate a student instance
    """
    def __init__(self, name, waiting_time):
        """
        Construct a new student that contains necessary information

        Parameters:
            name: the student name
            waiting_time: the time that this student has been waiting
        """
        self._name = name
        self._question_asked = 0
        self._is_in_queue = False
        self._start_time = None
        self._waiting_time = waiting_time
        self._elapsed_time = 0

    @property
    def info(self):
        """
        Return:
            a list contains some student information that will be displayed in the student table
        """
        return [self._name, self._question_asked, self._waiting_time]

    def increase_asked_ques(self):
        """
        the question asked attr will plus one
        """
        self._question_asked += 1

    def store_widget(self, widget):
        """
        Store relative widget in that student instance
        """
        self._widget = widget

    def __str__(self):
        """
        Display basic information of that student
        """
        return f'student: name:{self._name}, questions:{self._question_asked}, time:{self._waiting_time}'

    def set_in_queue(self):
        """
        Mark that student to be in the queue
        """
        self._is_in_queue = True

    def set_not_in_queue(self):
        """
        Mark that student not in the queue
        """
        self._is_in_queue = False

    def set_start_time(self):
        """
        Set the start waiting time when the student is in the queue
        """
        if self._is_in_queue:
            self._start_time = time.time()

    def clear_start_time(self):
        """
        Clear the start waiting time when student is not in the queue
        """
        if not self._is_in_queue:
            self._start_time = None

    def clear_waiting_info(self):
        """
        Clear student waiting information
        """
        self._waiting_time = 'a few seconds ago'

    def clear_elapsed_time(self):
        """
        Clear the elapsed time
        """
        self._elapsed_time = 0

    def start_track(self):
        """
        Start to track student's waiting time
        """
        self.set_in_queue()
        self.set_start_time()

    def clear_track(self):
        """
        Clear all the track when student is removed from the queue
        """
        self.set_not_in_queue()
        self.clear_start_time()
        self.clear_waiting_info()
        self.clear_elapsed_time()

    def track_time(self):
        """
        Keep track the student's waiting time and do actions when the elapsed_time changed

        Returns:
            elapsed_time
        """
        elapsed_time = 0
        if self._start_time is not None:
            elapsed_time = (float(time.time()) - float(self._start_time))/60
            elapsed_time = math.floor(elapsed_time)
            if 0 <= elapsed_time < 1:
                self._waiting_time = 'a few seconds ago'
            elif 1 <= elapsed_time < 2:
                self._waiting_time = 'a minute ago'
            elif 2 <= elapsed_time < 60:
                self._waiting_time = f'{str(elapsed_time)} minutes ago'
            elif 60 <= elapsed_time < 120:
                self._waiting_time = '1 hour ago'
            else:
                hours = math.floor(elapsed_time/60)
                self._waiting_time = f'{str(hours)} hours ago'
        self._elapsed_time = elapsed_time
        return elapsed_time

    def modify_row_time(self):
        """
        Modify the stored student row widget's waiting time text
        """
        row = self._widget
        time_label = list(row.children.values())[3]
        time_label.config(text=self._waiting_time)

    __repr__ = __str__


class StudentQueue:
    """
    A class to generate a student queue
    """
    def __init__(self):
        """
        Construct a new queue
        """
        self._queue = []

    def size(self):
        """
        Return:
            the size of the queue
        """
        return len(self._queue)

    def add_student(self, student):
        """
        Add a new student into the queue

        Parameter:
            student: student instance

        """
        self._queue.append(student)

    def find_by_name(self, name):
        """
        Iterator the queue and find the suitable student by name

        Return:
            the relative student instance
        """
        for student in self._queue:
            if name == student._name:
                return student
        return None

    def remove_by_name(self, name):
        """
        Remove the student from queue based on his/her name

        Parameter:
            name: the name of the student
        """
        student = self.find_by_name(name)
        self._queue.remove(student)
        return student

    def get_students(self):
        """
        Return
            (list) containing all the student instance
        """
        return self._queue

    def sort_queue(self):
        """
        Sort the queue first by question asked then by elapsed time
        """
        students = self._queue

        # sort by time first [10, 6, 2]
        students.sort(key=attrgetter('_elapsed_time'), reverse=True)

        # sort by asked question [0, 1, 2]
        students.sort(key=attrgetter('_question_asked'))


class Menu:
    """
    A class to generate a menu at the top of the window
    """
    def __init__(self, master):
        """
        Construct a new menu that user could play game by click a tab bar
        """
        menubar = tk.Menu(master)
        master.config(menu=menubar)

        gamemenu = tk.Menu(menubar)
        menubar.add_cascade(label="Game", menu=gamemenu)
        gamemenu.add_command(label="New Game", command=self.new_game)
        gamemenu.add_separator()
        gamemenu.add_command(label="Quit", command=self.close)

    def new_game(self):
        """
        Start the new game window
        """
        self.game_window = tk.Toplevel()
        self.game_window.title("Simple Break out game")

        game_app = GameApp(self.game_window)
        game_app.pack()

    def close(self):
        """
        Close the game window
        """
        self.game_window.destroy()


class QueueApp:
    """
    A class to initialize the queue App
    """
    INTERVAL = 10000

    def __init__(self, master):
        """
        Construct a new game app with all the widget installed and the queue arranged
        """
        self._master = master
        master.title('Queue App')

        self._quick_queue = StudentQueue()
        self._long_queue = StudentQueue()
        self._quick_queue_records = StudentQueue()
        self._long_queue_records = StudentQueue()

        self._menu = Menu(master)

        title = Title(master)
        title.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        headline = HeadLine(master)
        headline.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        description = Description(master)
        description.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        request = Request(master)
        request.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self._queue_info = QueueInfo(master)
        self._queue_info.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        student_table_caption = StudentTableCaption(master)
        student_table_caption.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self._student_table = StudentTable(master)
        self._student_table.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.update()

    def get_student_table(self):
        """
        Return:
              the student table
        """
        return self._student_table

    def get_quick_queue(self):
        """
        Return:
              the quick queue
        """
        return self._quick_queue

    def get_long_queue(self):
        """
        Return:
              the long queue
        """
        return self._long_queue

    def get_quick_queue_records(self):
        """
        quick queue records will store the history of a student once the student has joined the quick queue
        Return:
              the quick queue records,
        """
        return self._quick_queue_records

    def get_long_queue_records(self):
        """
        long queue records will store the history of a student once the student has joined the long queue
        Return:
              the long queue records,
        """
        return self._long_queue_records

    def update_quick_student_table(self):
        """
        Update the quick student table information based on student's information
        """
        students = self._quick_queue.get_students()
        length = len(students)
        display_content = 'No students in queue'
        if length > 0:
            total_time = 0
            for student in students:
                elapsed_time = student.track_time()
                student.modify_row_time()
                total_time += elapsed_time
            average_time = total_time / length
            # display average time
            display_content = f'{str(int(average_time))} average waiting minutes for {str(length)} students'
        self._queue_info.set_quick_info_content(display_content)

    def update_long_student_table(self):
        """
        Update the long student table information based on student's information
        """
        students = self._long_queue.get_students()
        length = len(students)
        display_content = 'No students in queue'
        if length > 0:
            total_time = 0
            for student in students:
                elapsed_time = student.track_time()
                student.modify_row_time()
                total_time += elapsed_time
            average_time = total_time / length
            # display average time
            display_content = f'{str(int(average_time))} average waiting minutes for {str(length)} students'
        self._queue_info.set_long_info_content(display_content)

    def update(self):
        """
        Update all the information for both queue when the time is updated
        """
        self.update_quick_student_table()
        self.update_long_student_table()
        self._master.after(self.INTERVAL, self.update)


if __name__ == "__main__":
    """
    The main function
    """
    root = tk.Tk()
    app = QueueApp(root)
    root.resizable(False, False)
    root.mainloop()
