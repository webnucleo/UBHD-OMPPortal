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
        redirect( URL('home', 'index'))
    series_path = request.args[0]
    
    if exists(request.folder+'views/series/'+series_path+"_info.html"):
        content = "series/"+series_path+"_info.html"
    else:
        redirect( URL('home', 'index'))
        
    return locals()

def index():
    if session.forced_language == 'en':
        locale = 'en_US'
    elif session.forced_language == 'de':
        locale = 'de_DE'
    else:
        locale = ''
        
    ompdal = OMPDAL(db, myconf)
    
    # Load press info from config
    press = ompdal.getPress(myconf.take('omp.press_id'))
    if not press:
        redirect(URL('home', 'index'))
    
    all_series = []
    for row in ompdal.getSeriesByPress(press.press_id):
        all_series.append(OMPItem(row, OMPSettings(ompdal.getSeriesSettings(row.series_id)), 
            {'series_editors': [OMPItem(u, OMPSettings(ompdal.getUserSettings(u.user_id))) 
                                for u in ompdal.getSeriesEditors(press.press_id, row.series_id)]}))
        
    all_series.sort(key=lambda s: s.settings.getLocalizedValue('title', locale))
    
    return locals()
