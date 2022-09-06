from tkinter import *

import mysql.connector
from DBConnection import database_name, user, password


class FirstWindow:
    def __init__(self, master):
        master.title("Lab 5/6")
        master.geometry("300x100")

        frame = Frame(master)
        frame.pack(fill=X)

        self.btn1 = Button(frame, text="Add a cartoon", command=self.open_window)
        self.btn1.pack(fill=BOTH)
        self.quitBtn = Button(frame, text="Quit", command=frame.quit)
        self.quitBtn.pack(fill=BOTH)

    @staticmethod
    def open_window():
        root1.destroy()
        root2 = Tk()
        SecondWindow(root2)
        root1.mainloop()


class SecondWindow(FirstWindow):

    def __init__(self, master):
        master.protocol("WM_DELETE_WINDOW", self.close)

        frame_top = Frame(master)
        frame_top.pack()
        frame1 = Frame(master)
        frame1.pack(side=TOP, fill=BOTH)

        self.label = Label(frame_top, text="Cartoon name: ")
        self.label.grid(row=0, column=0, sticky=E)
        self.label1 = Label(frame_top, text="Year of publishing: ")
        self.label1.grid(row=1, column=0, sticky=E)
        self.label2 = Label(frame_top, text="Duration: ")
        self.label2.grid(row=2, column=0, sticky=E)
        self.label3 = Label(frame_top, text="Producer: ")
        self.label3.grid(row=3, column=0, sticky=E)

        self.txt = Entry(frame_top)
        self.txt.grid(row=0, column=1)
        self.txt1 = Entry(frame_top)
        self.txt1.grid(row=1, column=1)
        self.txt2 = Entry(frame_top)
        self.txt2.grid(row=2, column=1)
        self.txt3 = Entry(frame_top)
        self.txt3.grid(row=3, column=1)

        self.btn1 = Button(frame1, text="Save", command=self.write_to_file)
        self.btn1.pack(fill=X)
        self.showBtn = Button(frame1, text="Show", command=self.show_btn_click)
        self.showBtn.pack(fill=X)
        self.delBtn = Button(frame1, text="Delete by name", command=self.delete_by_name)
        self.delBtn.pack(fill=X)
        self.closeBtn = Button(frame1, text='Close', command=self.close)
        self.closeBtn.pack(fill=X)

    def write_to_file(self):
        conn = mysql.connector.connect(
            host='localhost',
            database=database_name,
            user=user,
            password=password)
        cursor = conn.cursor()
        add_cartoon = ("INSERT INTO cartoon"
                       "(name, year, duration, producer) "
                       "VALUES (%s, %s, %s, %s)")

        data_cartoon = (self.txt.get(), self.txt1.get(), self.txt2.get(), self.txt3.get())

        cursor.execute(add_cartoon, data_cartoon)

        conn.commit()
        cursor.close()
        conn.close()

    def delete_by_name(self):
        conn = mysql.connector.connect(
            host='localhost',
            database=database_name,
            user=user,
            password=password)
        cursor = conn.cursor()

        delete_by_name = "DELETE FROM cartoon WHERE name = %s "

        cartoon_name = (self.txt.get())

        cursor.execute(delete_by_name, (cartoon_name, ))

        conn.commit()
        cursor.close()
        conn.close()

    def show_btn_click(self):
        conn = mysql.connector.connect(
            host='localhost',
            database=database_name,
            user=user,
            password=password)
        cursor = conn.cursor(buffered=True)

        query = "SELECT * FROM cartoon"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def close():
        root1.quit()


if __name__ == "__main__":
    root1 = Tk()
    root1.title("Lab 7/8")
    a = FirstWindow(root1)
    root1.mainloop()
