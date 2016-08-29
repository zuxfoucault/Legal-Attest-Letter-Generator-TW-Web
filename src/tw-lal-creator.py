#!/usr/bin/python
# -*- coding: utf-8 -*-
import pdfgenerator
import pdfmerger

LAL_FORMAT_PATH = '../res/tw_lal.pdf'
GENERATED_TEXT_PATH = 'content.pdf'
PDF_INCH = 72
A4_WIDE = 8.2677 * PDF_INCH
A4_HEIGHT = 11.692 * PDF_INCH
CONTENT_X_BEGIN = 1.27 * PDF_INCH
CONTENT_Y_BEGIN = 7.82 * PDF_INCH
CONTENT_X_INTERVAL = 0.33 * PDF_INCH
CONTENT_Y_INTERVAL = 0.47 * PDF_INCH
CONTENT_X_FIX = 0.001 * PDF_INCH
CONTENT_Y_FIX = 0.001 * PDF_INCH

generator = pdfgenerator.PDFgenerator(GENERATED_TEXT_PATH, A4_WIDE, A4_HEIGHT)
generator.setFont('/Library/Fonts/Arial Unicode.ttf', 20)
text = u'請於函到後五日內，主動與本人聯絡，並賠償'
x_begin = CONTENT_X_BEGIN
y_begin = CONTENT_Y_BEGIN
for i in range(0, len(text)):
    generator.drawString(x_begin, y_begin, text[i])
    x_begin += (CONTENT_X_INTERVAL + CONTENT_X_FIX)
generator.endThisPage()
generator.saveAndCloseFile()

merger = pdfmerger.PDFmerger(GENERATED_TEXT_PATH, LAL_FORMAT_PATH, 'output.pdf')
merger.mergeThenAdd(0, 0)
merger.save()
