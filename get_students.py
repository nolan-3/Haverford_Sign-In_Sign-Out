import csv

NAME_INDEX = 1
GRADE_INDEX = 2
PERIOD_INDEX = 3
EMAIL_INDEX = 4
# Returns the list of students who have the given free period first

class Student:
    def __init__(self, grade, email, signed_in=False):
        self.grade = grade
        self.signed_in = signed_in
        self.email = email

def get_students(period):
    students = {}

    # CSV data as a multi-line string
    # should include all fifth and sixth formers
    csv_data = """ID,name,grade,free,email
BARR042,"Barr, Thomas (Thomas)",V,A,thombarr@haverford.org
CAMP032,"Campbell, Reed (Reed)",V,A,reedcamp@haverford.org
CARS021,"Carson, Kenneth (Kenneth)",V,A,kenncars@haverford.org
ESPO011,"Esposito, Cameron (Cameron)",V,A,cameespo@haverford.org
HOIL011,"Hoilett, McKai (McKai)",V,A,mckahoil@haverford.org
KRAK011,"Krakovitz, Nicholas (Nick)",V,A,nichkrak@haverford.org
SAIA011,"Saial, Ali (Ali)",V,A,alisaia@haverford.org
SIMP011,"Simpkins, Connor (Connor)",V,A,connsimp@haverford.org
SULL051,"Sullivan, Quinn (Quinn)",V,A,quinsull@haverford.org
SUTE012,"Suter, William (Will)",V,A,willsute@haverford.org
TSIA011,"Tsiaras, Evangelos (Evan)",V,A,evantsia@haverford.org
WAI011,"Wai, Ryan (Ryan)",V,A,ryanwai@haverford.org
WANG061,"Wang, Simon (Simon)",V,A,simowang@haverford.org
WILL191,"Campbell-Williams, Colin (Colin)",V,A,colicamp@haverford.org
BART021,"Bartholdson, Anders (Anders)",VI,A,andebart@haverford.org
BONA011,"Bonaparte, Jai (Jai)",VI,A,jaibona@haverford.org
BROS012,"Brosko, Matthew (Matt)",VI,A,mattbros@haverford.org
BROW171,"Brown, Jey (Jey)",VI,A,jeybrow@haverford.org
CART031,"Carter, Anthony (Anthony)",VI,A,anthcart@haverford.org
COLS011,"Colsher, Ryan (Ryan)",VI,A,ryancols@haverford.org
CRES031,"Cresswell, Connor (Connor)",VI,A,conncres@haverford.org
FORT021,"Forte, Jackson (Jackson)",VI,A,jackfort@haverford.org
JABA011,"Jabateh, Musa (Musa)",VI,A,musajaba@haverford.org
KAPL042,"Kaplan, Thomas (Thomas)",VI,A,thomkapl@haverford.org
MIGN012,"Mignucci, Nicholas (Nicholas)",VI,A,nichmign@haverford.org
NEMO011,"Nemo, Alexander (Alex)",VI,A,alexnemo@haverford.org
PUTT011,"Putter, Lucas (Luke)",VI,A,lucaputt@haverford.org
ROSE072,"Rosenberger, Anthony (A.J.)",VI,A,anthrose@haverford.org
WOLI011,"Wolitarsky, James (William)",VI,A,jamewoli@haverford.org
BENS022,"Benson, Grey (Grey)",V,B,greybens@haverford.org
BORG011,"Borghese, Alexander (Alex)",V,B,alexborg@haverford.org
COVI011,"Covington, Kevin (Kevin)",V,B,kevicovi@haverford.org
HALP012,"Halpert, Charles (Charlie)",V,B,charhalp@haverford.org
PITT011,"Pitt, Bryce (Bryce)",V,B,brycpitt@haverford.org
CRES031,"Cresswell, Connor (Connor)",VI,B,conncres@haverford.org
CUDD021,"Cuddeback, John (Jack)",VI,B,johncudd@haverford.org
DUNB012,"Dunbar, Brandon (Brandon)",VI,B,brandunb@haverford.org
FEIG011,"Feigenberg, Matthew (Matthew)",VI,B,mattfeig@haverford.org
FORT021,"Forte, Jackson (Jackson)",VI,B,jackfort@haverford.org
HENG011,"Hengst, Austan (Austan)",VI,B,austheng@haverford.org
IBRA011,"Ibrahim, Amir (Amir)",VI,B,amiribra@haverford.org
JORD011,"Jordan, Frederick (Fred)",VI,B,fredjord@haverford.org
KOHL022,"Kohlenberg, John (John)",VI,B,johnkohl@haverford.org
MARR011,"Marr, Maximillian (Max)",VI,B,maximarr@haverford.org
MORA031,"Moran, Ryan (Ryan)",VI,B,ryanmora@haverford.org
RAYE011,"Rayer, William (Billy)",VI,B,willraye@haverford.org
SHAF011,"Shaffer, Reilly (Reilly)",VI,B,reilshaf@haverford.org
VALE011,"Valentino, Anthony (Anthony)",VI,B,anthvale@haverford.org
VOGE011,"Vogel, Tanner (Tanner)",VI,B,tannvoge@haverford.org
YOUN052,"Young, Banks (Banks)",VI,B,bankyoun@haverford.org
BECK041,"Becker, Jacob (Jacob)",V,C,jacobeck@haverford.org
BECK042,"Becker, Leo (Leo)",V,C,leobeck@haverford.org
CHIL011,"Childs, Reece (Reece)",V,C,reecchil@haverford.org
COHE041,"Cohen, Patrick (Pat)",V,C,patrcohe@haverford.org
CROW042,"Crowder, Gabriel (Gabriel)",V,C,gabrcrow@haverford.org
CRUT011,"Crutchlow, Michael (Michael)",V,C,michcrut@haverford.org
DECK031,"Decker, Colin (Colin)",V,C,colideck@haverford.org
DIXO011,"Dixon, Zachary (Zachary)",V,C,zachdixo@haverford.org
DOMB011,"Dombar, Simon (Simon)",V,C,simodomb@haverford.org
FERT011,"Fertels, Maxwell (Max)",V,C,maxwfert@haverford.org
FRED021,"Fredriksz, Hayden (Hayden)",V,C,haydfred@haverford.org
FUSC012,"Fuscaldo, Zachary (Zachary)",V,C,zachfusc@haverford.org
GANL011,"Ganley, Luke (Luke)",V,C,lukeganl@haverford.org
GILL081,"Gillis, Sebastian (Sebastian)",V,C,sebagill@haverford.org
GORD031,"Gordon, Avery (Avery)",V,C,avergord@haverford.org
GREE121,"Green, Robert (Brenner)",V,C,robegree@haverford.org
KANC011,"Kanchwala, Abdullah (Abdullah)",V,C,abdukanc@haverford.org
LAUX011,"Laux, Michael (Michael)",V,C,michlaux@haverford.org
LEE082,"Lee, Elliot (Elliot)",V,C,ellilee@haverford.org
LEE101,"Lee, Semaj (Semaj)",V,C,semalee@haverford.org
LI061,"Li, Kevin (Kevin)",V,C,kevili@haverford.org
LU011,"Lu, Nicholas (Nicholas)",V,C,nichlu@haverford.org
MCDA011,"McDade, Benjamin (Benjamin)",V,C,benjmcda@haverford.org
MILL121,"Millard, Mason (Mason)",V,C,masomill@haverford.org
MOUA011,"Moua, Zachary (Zach)",V,C,zachmoua@haverford.org
OKON011,"Okonkwo, Martin (Afam)",V,C,martokon@haverford.org
PENN011,"Pennington, Henry (Henry)",V,C,henrpenn@haverford.org
PENN022,"Pennewill, David (DJ)",V,C,davipenn@haverford.org
ROME021,"Romero, Thomas (TJ)",V,C,thomrome@haverford.org
ROSE011,"Rosenzweig, Ian (Ian)",V,C,ianrose@haverford.org
SCHU061,"Schulson, Davin (Davin)",V,C,davischu@haverford.org
STAI011,"Stait, Jamie (Jamie)",V,C,jamistai@haverford.org
VARM012,"Varma, Milan (Milan)",V,C,milavarm@haverford.org
WARD041,"Ward, Cameron (Cameron)",V,C,cameward@haverford.org
WHIT121,"White, Patrick (Patrick)",V,C,patrwhit@haverford.org
BELD011,"Belden, Daniel (Daniel)",VI,C,danibeld@haverford.org
BONA011,"Bonaparte, Jai (Jai)",VI,C,jaibona@haverford.org
BURF011,"Burfeind, William (Will)",VI,C,willburf@haverford.org
CERN011,"Cerniglia, Robert (Robert)",VI,C,robecern@haverford.org
CONK011,"Conklin, Mitchell (Tate)",VI,C,mitcconk@haverford.org
DELU011,"DeLuca, Alexander (Alec)",VI,C,alexdelu@haverford.org
FEIG011,"Feigenberg, Matthew (Matthew)",VI,C,mattfeig@haverford.org
FORD031,"Ford, Render (Render)",VI,C,rendford@haverford.org
GILD011,"Gildea, Thomas (Tom)",VI,C,thomgild@haverford.org
GLAS032,"Glaser, Andrew (Drew)",VI,C,andrglas@haverford.org
GREE131,"Green, William (Clayton)",VI,C,willgree@haverford.org
HERB011,"Herbert, Graeme (Graeme)",VI,C,graeherb@haverford.org
HOYT013,"Hoyt, Benjamin (Benjamin)",VI,C,benjhoyt@haverford.org
JACO032,"Jacobs, Keegan (Keegan)",VI,C,keegjaco@haverford.org
KAHA011,"Kahana, Nathan (Nathan)",VI,C,nathkaha@haverford.org
KEID011,"Keidel, Philip (Charlie)",VI,C,philkeid@haverford.org
KELL081,"Kelly, William (William)",VI,C,willkell@haverford.org
LYON031,"Lyon, Andrew (Andrew)",VI,C,andrlyon@haverford.org
MCCA102,"McCarthy, Benjamin (Ben)",VI,C,benjmcca@haverford.org
MCCO071,"McCoy, John (Thacher)",VI,C,johnmcco@haverford.org
MORA031,"Moran, Ryan (Ryan)",VI,C,ryanmora@haverford.org
MORR081,"Morris, Kyle (Kyle)",VI,C,kylemorr@haverford.org
OKAN011,"O'Kane, Brady (Brady)",VI,C,bradokan@haverford.org
REAV011,"Reavey, Kevin (Kevin)",VI,C,kevireav@haverford.org
RONO011,"Ronon, Gerald (Tripp)",VI,C,gerarono@haverford.org
SCAN011,"Scanlan, Connor (Connor)",VI,C,connscan@haverford.org
SEWA021,"Seward, William (Henry)",VI,C,willsewa@haverford.org
SHAT012,"Shatzman, Chase (Chase)",VI,C,chasshat@haverford.org
SMIT151,"Smith, Holden (Holden)",VI,C,holdsmit@haverford.org
STAL031,"Stallkamp, Brady (Brady)",VI,C,bradstal@haverford.org
STAM022,"Stamps, Gavin (Gavin)",VI,C,gavistam@haverford.org
STEW061,"Stewart, David (David)",VI,C,davistew@haverford.org
WATS041,"Watson, Luke (Luke)",VI,C,lukewats@haverford.org
WHIT111,"White, Michael (Ian)",VI,C,michwhit@haverford.org
WINI013,"Winikur, Asa (Asa)",VI,C,asawini@haverford.org
WYLI011,"Wylie, Michael (Michael)",VI,C,michwyli@haverford.org
YOH022,"Yoh, Russell (Russell)",VI,C,russyoh@haverford.org
BROD032,"Brodnik, Timothy (TJ)",IV,D,timobrod@haverford.org
CLAR061,"Clarke, Rauden (Rauden)",IV,D,raudclar@haverford.org
JONE151,"Jones, Matthew (Matt)",IV,D,mattjone@haverford.org
BIRC011,"Birch, Zahmir (Zahmir)",V,D,zahmbirc@haverford.org
BOUC011,"Bouchard, Nicholas (Nick)",V,D,nichbouc@haverford.org
CARP021,"Carpenter, Devin (Devin)",V,D,devicarp@haverford.org
DALT011,"Dalton, Connor (Connor)",V,D,conndalt@haverford.org
DEAN042,"Dean, James (James)",V,D,jamedean@haverford.org
DEGE012,"Degenhardt, Kai (Kai)",V,D,kaidege@haverford.org
GAFF021,"Gaffney, Thomas (Mac)",V,D,thomgaff@haverford.org
HARO012,"Haron, Myles (Myles)",V,D,myleharo@haverford.org
KANE031,"Kanefsky, Noah (Noah)",V,D,noahkane@haverford.org
KREY011,"Krey, Alexander (Alex)",V,D,alexkrey@haverford.org
LI011,"Li, Devon (Devon)",V,D,devoli@haverford.org
MANO011,"Manogue, Phineas (Phineas)",V,D,phinmano@haverford.org
MEYE041,"Meyer, Griffin (Griffin)",V,D,grifmeye@haverford.org
SAUL011,"Saul, Thomas (Tommy)",V,D,thomsaul@haverford.org
SIM011,"Sim, Lucas (Lucas)",V,D,lucasim@haverford.org
SMIT191,"Smith, Cameron (Cameron)",V,D,camesmit@haverford.org
WILL181,"Williams, Joshua (Josh)",V,D,joshwill@haverford.org
YERG011,"Yerger, Matthew (Matthew)",V,D,mattyerg@haverford.org
ANDR041,"Andrewson, Noah (Noah)",VI,D,noahandr@haverford.org
BAKE031,"Baker, Dawson (Dawson)",VI,D,dawsbake@haverford.org
BONG011,"Bongiovanni, Joseph (Quin)",VI,D,josebong@haverford.org
BREW012,"Brewington, Ryan (Ryan)",VI,D,ryanbrew@haverford.org
BROD031,"Brodnik, Sean (Sean)",VI,D,seanbrod@haverford.org
CIMI011,"Cimino, Richard (Jack)",VI,D,richcimi@haverford.org
CUDD021,"Cuddeback, John (Jack)",VI,D,johncudd@haverford.org
DIRO012,"DiRocco, Aydan (Aydan)",VI,D,aydadiro@haverford.org
GATE011,"Gates, James (James)",VI,D,jamegate@haverford.org
GILL061,"Gillespie, Connor (Connor)",VI,D,conngill@haverford.org
HARR061,"Harrington, Jackson (Jackson)",VI,D,jackharr@haverford.org
HOYT013,"Hoyt, Benjamin (Benjamin)",VI,D,benjhoyt@haverford.org
JIRU011,"Jiru, Samuel (Samuel)",VI,D,samujiru@haverford.org
KEID011,"Keidel, Philip (Charlie)",VI,D,philkeid@haverford.org
MCCL032,"McCloskey, Nolan (Nolan)",VI,D,nolamccl@haverford.org
MCCO051,"McComb, Benjamin (Ben)",VI,D,benjmcco@haverford.org
NAYA012,"Nayak, Adiyan (Adi)",VI,D,adiynaya@haverford.org
NEMO011,"Nemo, Alexander (Alex)",VI,D,alexnemo@haverford.org
NGO012,"Ngo, Sean (Sean)",VI,D,seanngo@haverford.org
PAUL031,"Paul, Blake (Blake)",VI,D,blakpaul@haverford.org
PERE011,"Perez-Gasiba, Sebastian (Sebastian)",VI,D,sebapere@haverford.org
PRYM011,"Pryma, Reilly (Reilly)",VI,D,reilprym@haverford.org
RALE012,"Raleigh, Jackson (Jackson)",VI,D,jackrale@haverford.org
RAYE011,"Rayer, William (Billy)",VI,D,willraye@haverford.org
ZHAN031,"Zhang, Max (Max)",VI,D,maxzhan@haverford.org
VAND031,"Vandiver, Henry (Henry)",IV,E,henrvand@haverford.org
ZHAO011,"Zhao, Kaiser (Kaiser)",IV,E,kaiszhao@haverford.org
BART022,"Bartholdson, Michael (Michael)",V,E,michbart@haverford.org
BONA012,"Bonaparte, Aaron (Aaron)",V,E,aarobona@haverford.org
BONN022,"Bonner, Declan (Declan)",V,E,declbonn@haverford.org
BORA012,"Boratto, Evan (Evan)",V,E,evanbora@haverford.org
BOUC011,"Bouchard, Nicholas (Nick)",V,E,nichbouc@haverford.org
BROW201,"Brown, Harrison (Harrison)",V,E,harrbrow@haverford.org
BUSS012,"Busser, Robert (Robby)",V,E,robebuss@haverford.org
ERSK011,"Erskine, Benjamin (Ben)",V,E,benjersk@haverford.org
ESPO011,"Esposito, Cameron (Cameron)",V,E,cameespo@haverford.org
FREN011,"French, William (Liam)",V,E,willfren@haverford.org
GAFF021,"Gaffney, Thomas (Mac)",V,E,thomgaff@haverford.org
KELL072,"Kelly, Finn (Finn)",V,E,finnkell@haverford.org
MATU021,"Matuch, Alexander (Xan)",V,E,alexmatu@haverford.org
MCDO011,"McDonald, Conor (Conor)",V,E,conomcdo@haverford.org
MEYE041,"Meyer, Griffin (Griffin)",V,E,grifmeye@haverford.org
NOBL011,"Noble, Charles (Charlie)",V,E,charnobl@haverford.org
AGGA012,"Aggarwal, Arsh (Arsh)",VI,E,arshagga@haverford.org
BARN071,"Barnes-Pace, Michael (Mick)",VI,E,michbarn@haverford.org
BOWE031,"Bowers, Quintin (Quintin)",VI,E,quinbowe@haverford.org
BRAD061,"Bradley, Andrew (Andrew)",VI,E,andrbrad@haverford.org
BROS012,"Brosko, Matthew (Matt)",VI,E,mattbros@haverford.org
BROW171,"Brown, Jey (Jey)",VI,E,jeybrow@haverford.org
BURF011,"Burfeind, William (Will)",VI,E,willburf@haverford.org
DIRO012,"DiRocco, Aydan (Aydan)",VI,E,aydadiro@haverford.org
ETHE011,"Etherington, Lowen (Lowen)",VI,E,loweethe@haverford.org
FAN011,"Fan, Justin (Justin)",VI,E,justfan@haverford.org
FESN011,"Fesnak, Luke (Luke)",VI,E,lukefesn@haverford.org
GIBS021,"Gibson, Edward (Edward)",VI,E,edwagibs@haverford.org
GILD011,"Gildea, Thomas (Tom)",VI,E,thomgild@haverford.org
GROS031,"Gross, Adon (Adon)",VI,E,adongros@haverford.org
HERD022,"Herd, Joseph (Joseph)",VI,E,joseherd@haverford.org
INNI011,"Inniss, Andre (Andre)",VI,E,andrinni@haverford.org
JABA011,"Jabateh, Musa (Musa)",VI,E,musajaba@haverford.org
JONE071,"Jones, Matthew (Matty)",VI,E,mattjone@haverford.org
KAIS021,"Kaiser, Daniel (Daniel)",VI,E,danikais@haverford.org
KOHN011,"Kohn, Edwin (Eddie)",VI,E,edwikohn@haverford.org
LAVE021,"Laveran, Pierce (Pierce)",VI,E,pierlave@haverford.org
LAWR021,"Lawrence, Peter (Finn)",VI,E,petelawr@haverford.org
LEE081,"Lee, Ethan (Ethan)",VI,E,ethalee@haverford.org
LONG041,"Long, Jackson (Jack)",VI,E,jacklong@haverford.org
MARR011,"Marr, Maximillian (Max)",VI,E,maximarr@haverford.org
MCCA102,"McCarthy, Benjamin (Ben)",VI,E,benjmcca@haverford.org
MILE011,"Miles, Michael (Brady)",VI,E,michmile@haverford.org
MURP021,"Murphy, Brody (Brody)",VI,E,brodmurp@haverford.org
NAYA012,"Nayak, Adiyan (Adi)",VI,E,adiynaya@haverford.org
NELS041,"Nelson, Chase (Chase)",VI,E,chasnels@haverford.org
NOLE012,"Nolen, Connor (Connor)",VI,E,connnole@haverford.org
PESH011,"Peshek-Percec, Alexander (Alexander)",VI,E,alexpesh@haverford.org
POPK011,"Popky, Robert (Bobby)",VI,E,robepopk@haverford.org
ROSE072,"Rosenberger, Anthony (A.J.)",VI,E,anthrose@haverford.org
ROUS012,"Rouse, John (John)",VI,E,johnrous@haverford.org
SCHW031,"Schwarting, Christopher (Christopher)",VI,E,chrischw@haverford.org
WALK062,"Walker, William (William)",VI,E,willwalk@haverford.org
WU021,"Wu, Preston (Preston)",VI,E,preswu@haverford.org
BORD011,"Borden, Andrew (Andrew)",V,F,andrbord@haverford.org
DUSK011,"Duska, Ronald (Miguel)",V,F,ronadusk@haverford.org
JOHN041,"Johnson, Amir (Amir)",V,F,amirjohn@haverford.org
JONE072,"Jones, Preston (Preston)",V,F,presjone@haverford.org
LEAD011,"Leader, Elijah (Eli)",V,F,elijlead@haverford.org
NEKO012,"Nekoumand, Nicholas (Nic)",V,F,nichneko@haverford.org
WIEG011,"Wiegand, Mason (Mason)",V,F,masowieg@haverford.org
BART021,"Bartholdson, Anders (Anders)",VI,F,andebart@haverford.org
FEIL011,"Feild, Dalton (Dalton)",VI,F,daltfeil@haverford.org
FORD031,"Ford, Render (Render)",VI,F,rendford@haverford.org
GOLD051,"Golderer, Sebastian (Sebastian)",VI,F,sebagold@haverford.org
GREE131,"Green, William (Clayton)",VI,F,willgree@haverford.org
HAYN011,"Hayne, Nicholas (Nicholas)",VI,F,nichhayn@haverford.org
LAWR021,"Lawrence, Peter (Finn)",VI,F,petelawr@haverford.org
LONG041,"Long, Jackson (Jack)",VI,F,jacklong@haverford.org
MCCL032,"McCloskey, Nolan (Nolan)",VI,F,nolamccl@haverford.org
ROUS012,"Rouse, John (John)",VI,F,johnrous@haverford.org
SCAN011,"Scanlan, Connor (Connor)",VI,F,connscan@haverford.org
SHAF011,"Shaffer, Reilly (Reilly)",VI,F,reilshaf@haverford.org
STAM022,"Stamps, Gavin (Gavin)",VI,F,gavistam@haverford.org
TREX011,"Trexler, Noah (Noah)",VI,F,noahtrex@haverford.org
WHIT111,"White, Michael (Ian)",VI,F,michwhit@haverford.org
WILL072,"Williams, Casey (Casey)",VI,F,casewill@haverford.org
ALLE031,"Allen, Sean (Sean)",V,G,seanalle@haverford.org
AREL011,"Harvison, Harvey (Harvey)",V,G,harvharv@haverford.org
BAKE041,"Baker, Gabriel (Gabriel)",V,G,gabrbake@haverford.org
BLOC041,"Block, Brandon (Brandon)",V,G,branbloc@haverford.org
BONA012,"Bonaparte, Aaron (Aaron)",V,G,aarobona@haverford.org
BRIN011,"Brinkley, Dhakir (Dhakir)",V,G,dhakbrin@haverford.org
BURM011,"Burman, Nathaniel (Nate)",V,G,nathburm@haverford.org
CLOR023,"Cloran, Duke (Duke)",V,G,dukeclor@haverford.org
COOP051,"Cooper, Gavin (Gavin)",V,G,gavicoop@haverford.org
DARD011,"Dardarian, Alexander (Alexander)",V,G,alexdard@haverford.org
FARR021,"Farrington, Ethan (Ethan)",V,G,ethafarr@haverford.org
GARD031,"Gardner, Kellen (Kellen)",V,G,kellgard@haverford.org
GERG011,"Gergo, Peter (Peter)",V,G,petegerg@haverford.org
GOEN011,"Goens, Robert (Robert)",V,G,robegoen@haverford.org
GORD041,"Gord, Charles (Charlie)",V,G,chargord@haverford.org
GRAN031,"Grant, Edmund (Eddie)",V,G,edmugran@haverford.org
HANE011,"Haney, Connor (Connor)",V,G,connhane@haverford.org
HOBA011,"Hoban, Joseph (JP)",V,G,josehoba@haverford.org
HOPE011,"Hope, Reilly (Reilly)",V,G,reilhope@haverford.org
JONE081,"Jones, Avery (Avery)",V,G,averjone@haverford.org
KOEN012,"Koenig, Harry (Harry)",V,G,harrkoen@haverford.org
LARG021,"Large, Evan (Evan)",V,G,evanlarg@haverford.org
LU011,"Lu, Nicholas (Nicholas)",V,G,nichlu@haverford.org
MCCL053,"McClave, Jude (Jude)",V,G,judemccl@haverford.org
OSWA011,"Oswald, Zachary (Zack)",V,G,zachoswa@haverford.org
PATT031,"Patterson, Christos (Christos)",V,G,chripatt@haverford.org
RHOD031,"Rhodes, Alexander (Alex)",V,G,alexrhod2@haverford.org
ROGE043,"Rogers, Jay (Jay)",V,G,jayroge@haverford.org
SHAR032,"Sharma, Unnav (Unnav)",V,G,unnashar@haverford.org
SWEI011,"Swei, Preston (Preston)",V,G,presswei@haverford.org
TIER013,"Tierney, Finnegan (Finn)",V,G,finntier@haverford.org
WATE011,"Waters, Kwamen (Kwamen)",V,G,kwamwate@haverford.org
WEIS043,"Weissenberger, Gregor (Gregor)",V,G,gregweis@haverford.org
WIED012,"Wiedmer, Alistair (Alistair)",V,G,aliswied@haverford.org
JACO032,"Jacobs, Keegan (Keegan)",VI,G,keegjaco@haverford.org
KRIE011,"Kriebel, Garrett (Garrett)",VI,G,garrkrie@haverford.org
LYON031,"Lyon, Andrew (Andrew)",VI,G,andrlyon@haverford.org
MURP021,"Murphy, Brody (Brody)",VI,G,brodmurp@haverford.org
PERE011,"Perez-Gasiba, Sebastian (Sebastian)",VI,G,sebapere@haverford.org
REAV011,"Reavey, Kevin (Kevin)",VI,G,kevireav@haverford.org
WOLI011,"Wolitarsky, James (William)",VI,G,jamewoli@haverford.org"""

    # creating a csv reader object from the multi-line string
    csvreader = csv.reader(csv_data.split('\n'))

    # extracting field names through first row,
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        free = row[PERIOD_INDEX]
        grade = row[GRADE_INDEX]
        name = row[NAME_INDEX]
        email = row[EMAIL_INDEX]

        students[name] = {"signed_in": True, "checked_out": False, "checked_in": False, "grade": grade, "email": email}
    csvreader = csv.reader(csv_data.split('\n'))

    # if the student doesn't have free period first they will be marked present by their teacher
    # if the student has free period first they must sign in using this app
    #fields = next(csvreader)

    for row in csvreader:
        free = row[PERIOD_INDEX]
        name = row[NAME_INDEX]
        #print(f"{name} has free period {free}")

        if free == period:
            students[name]["signed_in"] = False

    for student in students:
        if students[student]["signed_in"] == False:
            print(student)
    return students