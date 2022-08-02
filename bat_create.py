
WINDOWS = "windows"
MAC = "mac"

def return_path(SELECTED_OS, FILE_NAME):
    """OSごとに異なるパスを返す関数

    Keyword arguments:
    SELECTED_OS -- ユーザが選んだOS
    FILE_NAME -- ユーザが指定したファイル名
    Return: path
    """
    path = ""
    file_name = FILE_NAME
    if SELECTED_OS == WINDOWS:
        path= "./static/files/"+WINDOWS+"/"+file_name+".bat"
    else:
        path= "./static/files/"+MAC+"/"+file_name+".command"
    return path


def get_extensions(input_lines):
    """拡張機能を取得し、機能名のリストと機能数を返す関数

    Keyword arguments:
    inputlines -- フォームから取得した文字列
    Return: 拡張機能名:exts,拡張機能数:exts_n
    """
    # 拡張機能を入力された分だけ取得
    # print("拡張機能を改行ありで貼り付けて下さい\n[Enterで入力終了します]")
    exts = input_lines.split()
    exts_n = len(exts)
    # print("入力された機能数は"+str(exts_n)+"でした")
    return exts,exts_n


def create_body(select_os,exts, exts_n):
    """バッチファイルの内容を作る関数
    
    Keyword arguments:
    select_os -- ユーザが指定したOS
    exts -- 拡張機能名のリスト
    exts_n -- 拡張機能数
    Return: ファイルの内容:body
    """
    # windows
    if select_os == WINDOWS:
        # バッチファイルに書き込む内容の作成
        body = "@echo off\necho start to install VSCode extentions.\n"
        for i in range(exts_n):
            body+="code --install-extension "+exts[i].replace("\"", "")+" & "
            if i==exts_n-1:
                body+="echo finish installing... & pause\n"
        body+="exit"
    # mac
    else :
        body = "exts = (\n"
        for i in range(exts_n):
            body += "\""+exts[i]+"\"\n"
        body += ")\n"
        body += "cmd=\"code\"\n"
        body += "for ext in \"${exts\[@\]}\" ; do\n"
        body += "\tcmd=\"$cmd --install-extension $ext\"\n"
        body += "done\n"
        body += "eval $cmd"
    return body


def create_file(path, body):
    """ファイルを作成する関数
    
    Keyword arguments:
    path -- 作成するファイルのパス
    body -- ファイルの内容
    Return: none
    """
    
    # file作成, 書き込み, 終了
    file = open(path, 'w')
    file.write(body)
    file.close()
    # print(path+"にファイルを生成しました。")