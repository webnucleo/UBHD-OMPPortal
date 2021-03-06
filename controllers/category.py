# -*- coding: utf-8 -*-
'''
Copyright (c) 2015 Heidelberg University Library
Distributed under the GNU GPL v3. For full terms see the file
LICENSE.md
'''

from ompdal import OMPDAL, OMPSettings, OMPItem
from os.path import exists


def info():
    if request.args == []:
        redirect(URL('home', 'index'))
    category_path = request.args[0]
    press = ompdal.getPress(myconf.take('omp.press_id'))

    content = []
    category = []

    if exists(request.folder + 'views/catalog/' + category_path + "_info.html"):
        content = "category/" + category_path + "_info.html"
    else:
        category_row = ompdal.getCategoryByPathAndPress(category_path, press.press_id)
        category = OMPItem(category_row,
                           OMPSettings(ompdal.getCategorySettings(category_row.category_id))
                           )

    submission_rows = ompdal.getSubmissionsByCategory(category_row.category_id, ignored_submission_id=-1, status=3)


    return locals()
