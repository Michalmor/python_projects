# -*- coding: utf-8 -*-

import csv


class Mycsv:

    @staticmethod
    def writeList(path, data):
        # open the file in the write mode
        f = open(path, 'a',newline='')

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(data)

        # close the file
        f.close()

    def writeElements(path, data):
        # open the file in the write mode
        f = open(path, 'w')

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        for e in data:
            writer.writerow([e])

        # close the file
        f.close()

    @staticmethod
    def read(path):
        data = []
        with open(path , 'r', encoding="utf8") as f:
            csv_reader = csv.reader(f,dialect='excel')
            for line in csv_reader:
                data += [line]
        return data

    def reset(path, data = []):
        # open the file in the write mode
        f = open(path, 'w',newline='')

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(data)

        # close the file
        f.close()