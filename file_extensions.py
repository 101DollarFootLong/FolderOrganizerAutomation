def getExtDict():
    main_EXT_dict = {}
    main_EXT_dict[ "AUDIO"] = ["aif", ".cda", "mid", "mp3", "mpa", "ogg", 'wav', "wma", "wpl"]
    main_EXT_dict[ "VIDEO"] = [".mp4", ".m4a", ".m4v", "f4v", ".f4a", ".m4b", "m4r", ".mov", ".avi", "wmv", ".flv"]
    main_EXT_dict[ "IMAGES"] = [".jpeg", ".png", ".svg", "gif", ".bmp"]
    main_EXT_dict[ "ADOBE"] = [".psd", ".ae", ".pr"]
    main_EXT_dict[ "DOCUMENTS"] = [".pdf", ".doc", ".txt", ",docx", ".html"]
    main_EXT_dict[ "DATA"] = [".csv", ".xlsx"]
    return main_EXT_dict