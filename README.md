# NPCGenerator4e
NPC Generator for Warhammer Fantasy Roleplay Fourth Edition

note: all the values/info are hardcoded. This started as a small project that has been steadily growing. At this point, it's 
easier to keep using that format than it is refactoring.

modified files for 1.2:
extra_books, career info, talent info, npccreator, talents, species, names, finalDetails, name_info, forms, career

 The core function for the generator is the CreateCharacter function, in base.py. It calls the many functions within the repository in order to create an NPC. The data itself (career specifics, detailed skills etc) is in the info folder. 
 
to add new books:
 add them to info/extra_books.py, following the format within. Then, add them in /forms.py on book_list
  
  For careers, add them to info.career_info, following the format within. Then, add the event listener and function 
  in npccreator.html (I couldn't get pythonanywhere to detect the js file, so I had to embed it there)

  for species, add them into the book dictionary in extra_books.py. Later, you'll have to enter the corresponding exception on
  species, names, finalDetails, in case of being an elf, dwarf, halfling or human

  If there are new skills/talents, make sure to add them on info.detailed_skills or info.talent_info


  10.2:
   Added careers and species from Up in Arms. Should be working reasonably well. 
   The tilean names were taken from a Warhammer Fantasy Wiki and Up in Arms, plus a few more Italian names for women, since otherwise there'd be too few of them
   Pending bug: when creating a character from a non-core species, the species selector unchecks itself. 
