
from extract_data import Extracting_data
from make_word import Word_docx
from translate import Translate
from user_interfase import Menu
if __name__ == "__main__":
    UI=Menu()
    UI.welcome()
    UI.options()
    links=UI.get_links()
    for i in range(len(links)):
        
      Start=Extracting_data('images',links[i])
      #Start=Extracting_data('images',"https://thehackernews.com/2023/12/new-chameleon-android-banking-trojan.html")
      Start.delete_files_in_folder_before_parsing()
      Start.parsing_thehackernews()
      titletext=Start.get_titletext()
      maintext=Start.get_maintext()
      tags=Start.get_tags()
      li=Start.get_li()
      link=Start.get_link()
      folder=Start.get_foledr()
      imgname=Start.get_imgname()


      Google_translate=Translate(maintext,li,titletext)
      Google_translate.translate()
      main_text_polish=Google_translate.get_polish()
      li_text_polish=Google_translate.get_polish_li()
      polish_title=Google_translate.get_polish_title()
      Word=Word_docx(folder,link,polish_title,main_text_polish,tags,li_text_polish,imgname,i)
      Word.word_format()
    Word.merge()



    