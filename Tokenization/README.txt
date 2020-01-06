i.
    a. The hardest part I encountered in this assignment was to extract the word from raw html file with regular expression.
    b. The easiest part is the logic of this assignment.
ii.
    a. The TermIDFile is designed using dictionary, which I map every term to the document frequency. The termID is obtained by the index of its dictionary.
    b. The DocumentIDFile is designed using dictionary as well, it maps a document ID (an integer) to the another dictionary which has its name as key and the number of tokens contained in the document as value.
    c. The InvertedIndex is designed using dictionary, it maps terms to another dictionary which contains document IDs as keys and the frequencies of the term occurs in the document as value.
iii.
    The query that I tried is "Karen research crawler"
    The result is attached below
iv.
    None

Result for iii:

The term we search for is:                            Karen
The ID associated with the term is:                   0
The list of document that the term appears in are:    {1: 3, 5: 1, 10: 2, 18: 2, 21: 1, 33: 1, 34: 1, 61: 3, 143: 2, 146: 2, 149: 2, 235: 1, 389: 1, 398: 1, 412: 1, 436: 1, 473: 1, 487: 1, 560: 1, 636: 1, 675: 2, 702: 1, 764: 1, 892: 1, 909: 1, 967: 3}
ID:  1  Document Name:  Karen Spärck Jones - Wikipedia
ID:  5  Document Name:  Roger Needham - Wikipedia
ID:  10  Document Name:  tf–idf - Wikipedia
ID:  18  Document Name:  tf–idf - Wikipedia
ID:  21  Document Name:  University of Huddersfield - Wikipedia
ID:  33  Document Name:  Evgeniy Gabrilovich - Wikipedia
ID:  34  Document Name:  Diane Kelly (computer scientist) - Wikipedia
ID:  61  Document Name:  Karen Spärck Jones - Wikipedia
ID:  143  Document Name:  The Guardian - Wikipedia
ID:  146  Document Name:  Denmark - Wikipedia
ID:  149  Document Name:  Denmark - Wikipedia
ID:  235  Document Name:  Pen name - Wikipedia
ID:  389  Document Name:  Huddersfield (UK Parliament constituency) - Wikipedia
ID:  398  Document Name:  England - Wikipedia
ID:  412  Document Name:  Huddersfield (UK Parliament constituency) - Wikipedia
ID:  436  Document Name:  University of Huddersfield - Wikipedia
ID:  473  Document Name:  Huddersfield (UK Parliament constituency) - Wikipedia
ID:  487  Document Name:  Happy Valley (TV series) - Wikipedia
ID:  560  Document Name:  Asian people - Wikipedia
ID:  636  Document Name:  Dewsbury - Wikipedia
ID:  675  Document Name:  Bill Shankly - Wikipedia
ID:  702  Document Name:  University of Huddersfield - Wikipedia
ID:  764  Document Name:  University of Huddersfield - Wikipedia
ID:  892  Document Name:  Dewsbury - Wikipedia
ID:  909  Document Name:  Rothwell, West Yorkshire - Wikipedia
ID:  967  Document Name:  Karen Spärck Jones - Wikipedia

The term we search for is:                            research
The ID associated with the term is:                   169
The list of document that the term appears in are:    {1: 1, 6: 4, 7: 23, 11: 2, 13: 1, 15: 4, 16: 7, 17: 2, 19: 2, 21: 5, 22: 17, 23: 4, 24: 1, 25: 2, 26: 1, 29: 4, 31: 4, 32: 1, 33: 2, 34: 2, 35: 2, 36: 1, 38: 1, 39: 1, 42: 2, 46: 2, 47: 4, 48: 1, 49: 1, 55: 1, 56: 1, 57: 2, 59: 1, 60: 1, 61: 1, 66: 2, 99: 6, 110: 2, 114: 1, 122: 13, 126: 1, 130: 2, 132: 11, 134: 4, 136: 1, 143: 1, 146: 2, 149: 2, 161: 6, 162: 1, 164: 3, 169: 1, 170: 5, 171: 5, 175: 10, 186: 1, 195: 1, 208: 1, 225: 1, 230: 1, 235: 1, 241: 1, 242: 1, 248: 1, 298: 2, 351: 1, 352: 32, 356: 32, 358: 1, 362: 21, 363: 2, 365: 6, 370: 1, 371: 1, 372: 2, 375: 2, 396: 3, 398: 3, 399: 2, 418: 1, 419: 1, 420: 1, 427: 5, 430: 3, 436: 5, 446: 2, 447: 1, 455: 1, 461: 5, 465: 3, 467: 1, 468: 2, 474: 1, 481: 1, 562: 1, 567: 2, 569: 2, 572: 2, 575: 1, 580: 1, 583: 3, 585: 1, 594: 1, 637: 1, 643: 1, 691: 1, 694: 1, 702: 5, 722: 1, 741: 3, 742: 1, 743: 2, 748: 1, 754: 1, 755: 1, 764: 5, 765: 1, 774: 1, 776: 1, 777: 2, 781: 1, 782: 8, 790: 3, 817: 1, 824: 1, 834: 2, 837: 2, 843: 3, 853: 1, 882: 1, 944: 3, 947: 3, 950: 1, 962: 2, 963: 21, 967: 1, 970: 21, 972: 2, 973: 4, 974: 1, 975: 5, 978: 2, 979: 2, 982: 1, 983: 95, 984: 2, 985: 3, 986: 3, 987: 3, 988: 1, 992: 1, 994: 5, 996: 4, 997: 4, 998: 8, 999: 1, 1000: 13}
ID:  1  Document Name:  Karen Spärck Jones - Wikipedia
ID:  6  Document Name:  Department of Computer Science and Technology, University of Cambridge - Wikipedia
ID:  7  Document Name:  Thesis - Wikipedia
ID:  11  Document Name:  Web search engine - Wikipedia
ID:  13  Document Name:  World War II - Wikipedia
ID:  15  Document Name:  Department of Computer Science and Technology, University of Cambridge - Wikipedia
ID:  16  Document Name:  Natural language processing - Wikipedia
ID:  17  Document Name:  Information retrieval - Wikipedia
ID:  19  Document Name:  Alvey - Wikipedia
ID:  21  Document Name:  University of Huddersfield - Wikipedia
ID:  22  Document Name:  British Academy - Wikipedia
ID:  23  Document Name:  Association for the Advancement of Artificial Intelligence - Wikipedia
ID:  24  Document Name:  European Coordinating Committee for Artificial Intelligence - Wikipedia
ID:  25  Document Name:  Association for Computational Linguistics - Wikipedia
ID:  26  Document Name:  Gerard Salton Award - Wikipedia
ID:  29  Document Name:  Association for the Advancement of Artificial Intelligence - Wikipedia
ID:  31  Document Name:  Microsoft Research - Wikipedia
ID:  32  Document Name:  Mirella Lapata - Wikipedia
ID:  33  Document Name:  Evgeniy Gabrilovich - Wikipedia
ID:  34  Document Name:  Diane Kelly (computer scientist) - Wikipedia
ID:  35  Document Name:  Dictionary of National Biography - Wikipedia
ID:  36  Document Name:  Digital object identifier - Wikipedia
ID:  38  Document Name:  Journal of Documentation - Wikipedia
ID:  39  Document Name:  Digital object identifier - Wikipedia
ID:  42  Document Name:  Association for Computational Linguistics - Wikipedia
ID:  46  Document Name:  Makoto Nagao - Wikipedia
ID:  47  Document Name:  Martin Kay - Wikipedia
ID:  48  Document Name:  Biblioteca Nacional de España - Wikipedia
ID:  49  Document Name:  Bibliothèque nationale de France - Wikipedia
ID:  55  Document Name:  National Library of Australia - Wikipedia
ID:  56  Document Name:  Royal Library of the Netherlands - Wikipedia
ID:  57  Document Name:  LIBRIS - Wikipedia
ID:  59  Document Name:  Virtual International Authority File - Wikipedia
ID:  60  Document Name:  WorldCat - Wikipedia
ID:  61  Document Name:  Karen Spärck Jones - Wikipedia
ID:  66  Document Name:  United Kingdom - Wikipedia
ID:  99  Document Name:  Simon Baron-Cohen - Wikipedia
ID:  110  Document Name:  Basque Country (autonomous community) - Wikipedia
ID:  114  Document Name:  Spanish language - Wikipedia
ID:  122  Document Name:  Portugal - Wikipedia
ID:  126  Document Name:  José Manuel Barroso - Wikipedia
ID:  130  Document Name:  Germany - Wikipedia
ID:  132  Document Name:  Immigration - Wikipedia
ID:  134  Document Name:  Elisabeth Noelle-Neumann - Wikipedia
ID:  136  Document Name:  World War I - Wikipedia
ID:  143  Document Name:  The Guardian - Wikipedia
ID:  146  Document Name:  Denmark - Wikipedia
ID:  149  Document Name:  Denmark - Wikipedia
ID:  161  Document Name:  Poland - Wikipedia
ID:  162  Document Name:  Polish language - Wikipedia
ID:  164  Document Name:  Turkey - Wikipedia
ID:  169  Document Name:  Antonio Villaraigosa - Wikipedia
ID:  170  Document Name:  European Union - Wikipedia
ID:  171  Document Name:  France - Wikipedia
ID:  175  Document Name:  Quebec - Wikipedia
ID:  186  Document Name:  Scipio Vaughan - Wikipedia
ID:  195  Document Name:  Victorian era - Wikipedia
ID:  208  Document Name:  Mononymous person - Wikipedia
ID:  225  Document Name:  Pseudonym - Wikipedia
ID:  230  Document Name:  Pseudonym - Wikipedia
ID:  235  Document Name:  Pen name - Wikipedia
ID:  241  Document Name:  Naming in the United States - Wikipedia
ID:  242  Document Name:  African-American names - Wikipedia
ID:  248  Document Name:  Azerbaijani name - Wikipedia
ID:  298  Document Name:  Macedonian onomastics - Wikipedia
ID:  351  Document Name:  Post-nominal letters - Wikipedia
ID:  352  Document Name:  Academic degree - Wikipedia
ID:  356  Document Name:  Academic degree - Wikipedia
ID:  358  Document Name:  Chivalry - Wikipedia
ID:  362  Document Name:  List of academic ranks - Wikipedia
ID:  363  Document Name:  Honorary title (academic) - Wikipedia
ID:  365  Document Name:  Professional degree - Wikipedia
ID:  370  Document Name:  Acronym - Wikipedia
ID:  371  Document Name:  Anonymity - Wikipedia
ID:  372  Document Name:  Anthropomorphism - Wikipedia
ID:  375  Document Name:  Family - Wikipedia
ID:  396  Document Name:  Yorkshire and the Humber - Wikipedia
ID:  398  Document Name:  England - Wikipedia
ID:  399  Document Name:  United Kingdom - Wikipedia
ID:  418  Document Name:  College town - Wikipedia
ID:  419  Document Name:  Leeds - Wikipedia
ID:  420  Document Name:  Manchester - Wikipedia
ID:  427  Document Name:  Industrial Revolution - Wikipedia
ID:  430  Document Name:  Harold Wilson - Wikipedia
ID:  436  Document Name:  University of Huddersfield - Wikipedia
ID:  446  Document Name:  Europa Nostra - Wikipedia
ID:  447  Document Name:  Castra - Wikipedia
ID:  455  Document Name:  Anglo-Saxons - Wikipedia
ID:  461  Document Name:  Industrial Revolution - Wikipedia
ID:  465  Document Name:  Harold Wilson - Wikipedia
ID:  467  Document Name:  Green Party of England and Wales - Wikipedia
ID:  468  Document Name:  Conservative Party (UK) - Wikipedia
ID:  474  Document Name:  Barry Sheerman - Wikipedia
ID:  481  Document Name:  Agrochemical - Wikipedia
ID:  562  Document Name:  Bangladesh - Wikipedia
ID:  567  Document Name:  Church of England - Wikipedia
ID:  569  Document Name:  Methodism - Wikipedia
ID:  572  Document Name:  Buddhism - Wikipedia
ID:  575  Document Name:  Jehovah's Witnesses - Wikipedia
ID:  580  Document Name:  New Zealand - Wikipedia
ID:  583  Document Name:  Harold Wilson - Wikipedia
ID:  585  Document Name:  William Wallen (architect) - Wikipedia
ID:  594  Document Name:  Victorian era - Wikipedia
ID:  637  Document Name:  Leeds - Wikipedia
ID:  643  Document Name:  YMCA - Wikipedia
ID:  691  Document Name:  Choir - Wikipedia
ID:  694  Document Name:  Messiah (Handel) - Wikipedia
ID:  702  Document Name:  University of Huddersfield - Wikipedia
ID:  722  Document Name:  Henry Moore - Wikipedia
ID:  741  Document Name:  Woolworths Group - Wikipedia
ID:  742  Document Name:  KFC - Wikipedia
ID:  743  Document Name:  McDonald's - Wikipedia
ID:  748  Document Name:  Marks &amp; Spencer - Wikipedia
ID:  754  Document Name:  Burger King - Wikipedia
ID:  755  Document Name:  Marks &amp; Spencer - Wikipedia
ID:  764  Document Name:  University of Huddersfield - Wikipedia
ID:  765  Document Name:  Prince Andrew, Duke of York - Wikipedia
ID:  774  Document Name:  Terminal illness - Wikipedia
ID:  776  Document Name:  Emergency department - Wikipedia
ID:  777  Document Name:  Family planning - Wikipedia
ID:  781  Document Name:  Geriatrics - Wikipedia
ID:  782  Document Name:  Psychiatry - Wikipedia
ID:  790  Document Name:  Harold Wilson - Wikipedia
ID:  817  Document Name:  William Broadbent - Wikipedia
ID:  824  Document Name:  Cartography - Wikipedia
ID:  834  Document Name:  Conservative Party (UK) - Wikipedia
ID:  837  Document Name:  Harold Percival Himsworth - Wikipedia
ID:  843  Document Name:  Harold Wilson - Wikipedia
ID:  853  Document Name:  Vivek Murthy - Wikipedia
ID:  882  Document Name:  City of Bradford - Wikipedia
ID:  944  Document Name:  Cambridge - Wikipedia
ID:  947  Document Name:  Bronze Age - Wikipedia
ID:  950  Document Name:  Middle Ages - Wikipedia
ID:  962  Document Name:  United Kingdom - Wikipedia
ID:  963  Document Name:  University of Cambridge - Wikipedia
ID:  967  Document Name:  Karen Spärck Jones - Wikipedia
ID:  970  Document Name:  University of Cambridge - Wikipedia
ID:  972  Document Name:  David Wheeler (computer scientist) - Wikipedia
ID:  973  Document Name:  Ross J. Anderson - Wikipedia
ID:  974  Document Name:  Peter G. Gyarmati - Wikipedia
ID:  975  Document Name:  Andrew Herbert - Wikipedia
ID:  978  Document Name:  United Kingdom - Wikipedia
ID:  979  Document Name:  Computer scientist - Wikipedia
ID:  982  Document Name:  St John's College, Cambridge - Wikipedia
ID:  983  Document Name:  Doctor of Philosophy - Wikipedia
ID:  984  Document Name:  Computer - Wikipedia
ID:  985  Document Name:  Computer security - Wikipedia
ID:  986  Document Name:  Operating system - Wikipedia
ID:  987  Document Name:  Computer architecture - Wikipedia
ID:  988  Document Name:  Local area network - Wikipedia
ID:  992  Document Name:  Michael Schroeder - Wikipedia
ID:  994  Document Name:  Authentication - Wikipedia
ID:  996  Document Name:  Department of Computer Science and Technology, University of Cambridge - Wikipedia
ID:  997  Document Name:  Microsoft Research - Wikipedia
ID:  998  Document Name:  Fellow - Wikipedia
ID:  999  Document Name:  Wolfson College, Cambridge - Wikipedia
ID:  1000  Document Name:  Royal Society - Wikipedia

The term we search for is:                            crawler
The ID associated with the term is:                   4604
The list of document that the term appears in are:    {11: 4, 197: 4}
ID:  11  Document Name:  Web search engine - Wikipedia
ID:  197  Document Name:  Wayback Machine - Wikipedia

