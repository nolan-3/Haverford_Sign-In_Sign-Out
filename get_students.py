import csv

NAME_INDEX = 0
GRADE_INDEX = 1
PERIOD_INDEX = 2
EMAIL_INDEX = 3
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
    csv_data = """name,grade,free,email
"Friel, James ( James )",IV,A,jamefrie@haverford.org
"Aloi, Luca ( Luca )",V,A,lucaaloi@haverford.org
"Barr, Thomas ( Thomas )",V,A,thombarr@haverford.org
"Campbell, Reed ( Reed )",V,A,reedcamp@haverford.org
"Crutchlow, Michael ( Michael )",V,A,michcrut@haverford.org
"Dean, James ( James )",V,A,jamedean@haverford.org
"Decker, Colin ( Colin )",V,A,colideck@haverford.org
"Dixon, Zachary ( Zachary )",V,A,zachdixo@haverford.org
"Fredriksz, Hayden ( Hayden )",V,A,haydfred@haverford.org
"French, William ( Liam )",V,A,willfren@haverford.org
"Gillis, Sebastian ( Sebastian )",V,A,sebagill@haverford.org
"Hoilett, McKai ( McKai )",V,A,hoilmcka@haverford.org
"Kelly, Finn ( Finn )",V,A,finnkell@haverford.org
"Koenig, Harry ( Harry )",V,A,harrkoen@haverford.org
"Krakovitz, Nicholas ( Nick )",V,A,nichkrak@haverford.org
"Laux, Michael ( Michael )",V,A,michlaux@haverford.org
"Lee, Elliot ( Elliot )",V,A,ellilee@haverford.org
"Lu, Nicholas ( Nicholas )",V,A,nichlu@haverford.org
"Moua, Zachary ( Zach )",V,A,zachmoua@haverford.org
"Saial, Ali ( Ali)",V,A,alisaia@haverford.org
"Schulson, Davin ( Davin )",V,A,davischu@haverford.org
"Sullivan, Quinn ( Quinn )",V,A,quinsull@haverford.org
"Suter, William ( Will)",V,A,willsute@haverford.org
"Tsiaras, Evangelos ( Evan )",V,A,evantsia@haverford.org
"Varma, Milan ( Milan )",V,A,milavarm@haverford.org
"Wai, Ryan ( Ryan )",V,A,ryanwai@haverford.org
"Wang, Simon ( Simon )",V,A,simowang@haverford.org
"Wiegand, Mason ( Mason )",V,A,masowieg@haverford.org
"Campbell-Williams, Colin ( Colin )",V,colicamp@haverford.org
"Brosko, Matthew ( Matt )",VI,A,mattbros@haverford.org
"Conklin, Mitchell ( Tate )",VI,A,mitcconk@haverford.org
"Cuddeback, John ( Jack )",VI,A,johncudd@haverford.org
"DeLuca, Alexander ( Alec )",VI,A,alexdelu@haverford.org
"Glaser, Andrew ( Drew )",VI,A,andrglas@haverford.org
"Hoyt, Benjamin ( Benjamin )",VI,A,benjhoyt@haverford.org
"Jiru, Samuel ( Samuel )",VI,A,samujiru@ghaverford.org
"Jordan, Frederick ( Fred )",VI,A,fredjord@haverford.org
"McCarthy, Benjamin ( Ben )",VI,A,benjmcca@haverford.org
"Morris, Kyle ( Kyle )",VI,A,kylemorr@haverford.org
"Raleigh, Jackson ( Jackson )",VI,A,jackrale@haverford.org
"Rouse, John ( John )",VI,A,johnrous@haverford.org
"Stamps, Gavin ( Gavin )",VI,A,gavistam@haverford.org
"Stewart, David ( David )",VI,A,davistew@haverford.org
"Valentino, Anthony ( Anthony )",VI,A,anthvale@haverford.org
"Wylie, Michael ( Michael )",VI,A,michwyli@haverford.org
"Becker, Jacob ( Jacob )",V,B,jacobeck@haverford.org
"Becker, Leo ( Leo )",V,B,leobeck@haverford.org
"Borghese, Alexander ( Alex )",V,B,alexborg@haverford.org
"Brinkley, Dhakir ( Dhakir )",V,B,dhakbrin@haverford.org
"Childs, Reece ( Reece )",V,B,reecchil@haverford.org
"Ganley, Luke ( Luke )",V,B,lukeganl@haverford.org
"Gardner, Kellen ( Kellen )",V,B,kellgard@haverford.org
"Gergo, Peter ( Peter )",V,B,petegerg@haverford.org
"Green, Robert ( Brenner )",V,B,robegree@haverford.org
"Halpert, Charles ( Charlie )",V,B,charhalp@haverford.org
"Large, Evan ( Evan )",V,B,evanlarg@haverford.org
"McDonald, Conor ( Conor )",V,B,conomcdo@haverford.org
"Nekoumand, Nicholas ( Nic )",V,B,nichneko@haverford.org
"Oswald, Zachary ( Zack )",V,B,zachoswa@haverford.org
"Pitt, Bryce ( Bryce )",V,B,brycpitt@haverford.org
"Sim, Lucas ( Lucas )",V,B,lucasim@haverford.org
"Brown, Jey (Jey )",VI,B,jeybrow@haverford.org
"Cimino, Richard ( Jack )",VI,B,richcimi@haverford.org
"Cresswell, Connor ( Connor )",VI,B,conncres@haverford.org
"Dunbar, Brandon ( Brandon )",VI,B,brandunb@haverford.org
"Feigenberg, Matthew ( Matthew )",VI,B,mattfeig@haverford.org
"Forte, Jackson ( Jackson )",VI,B,jackfort@haverford.org
"Hayne, Nicholas ( Nicholas )",VI,B,nichhayn@haverford.org
"Ibrahim, Amir ( Amir )",VI,B,amiribra@haverford.org
"Kahana, Nathan ( Nathan )",VI,B,nathkaha@haverford.org
"Kelly, William ( William )",VI,B,willkell@haverford.org
"Kohlenberg, John ( John )",VI,B,johnkohl@haverford.org
"Lyon, Andrew ( Andrew )",VI,B,andrlyon@haverford.org
"Marr, Maximillian ( Max )",VI,B,maximarr@haverford.org
"Perez-Gasiba, Sebastian ( Sebastian )",VI,B,sebapere@haverford.org
"Popky, Robert ( Bobby )",VI,B,robepopk@haverford.org
"Schwarting, Christopher ( Christopher )",VI,B,chrischw@haverford.org
"Seward, William ( Henry )",VI,B,willsewa@haverford.org
"White, Michael (Ian )",VI,B,michwhit@haverford.org
"Costa, Anthony ( Anthony ),IV,C,anthcost@haverford.org
"Horwitz, Jacob ( Jacob )",IV,C,jacohorw@haverford.org
"Allen, Sean ( Sean )",V,C,seanalle@haverford.org
"Bouchard, Nicholas ( Nick )",V,C,nichbouc@haverford.org
"Gordon, Avery ( Avery )",V,C,avergord@haverford.org
"Grant, Edmund ( Eddie )",V,C,edmugran@haverford.org
"Lee, Semaj ( Semaj )",V,C,semalee@haverford.org
"Li, Kevin ( Kevin )",V,C,kevili@haverford.org
"McDade, Benjamin ( Benjamin )",V,C,benjmcda@haverford.org
"Okonkwo, Martin ( Afam )",V,C,martokon@haverford.org
"Pennington, Henry ( Henry )",V,C,henrpenn@haverford.org
"Rosenzweig, Ian ( Ian )",V,C,ianrose@haverford.org
"Ward, Cameron ( Cameron )",V,C,cameward@haverford.org
"White, Patrick ( Patrick ),V,C,patrwhit@haverford.org"
"Bartholdson, Anders ( Anders )",VI,C,andebart@haverford.org
"Bonaparte, Jai ( Jai)",VI,C,jaibona@haverford.org
"Brosko, Matthew ( Matt )",VI,C,mattbros@haverford.org
"Feild, Dalton ( Dalton )",VI,C,daltfeil@haverford.org
"Herbert, Graeme ( Graeme )",VI,C,graeherb@haverford.org
"Jabateh, Musa ( Musa )",VI,C,musajaba@haverford.org
"Kohn, Edwin ( Eddie )",VI,C,edwikohn@haverford.org
"McCarthy, Benjamin ( Ben )",VI,C,benjmcca@haverford.org
"McComb, Benjamin ( Ben )",VI,C,benjmcco@haverford.org
"McCoy, John ( Thacher )",VI,C,johnmcco@haverford.org
"Moran, Ryan ( Ryan )",VI,C,ryanmora@haverford.org
"Murphy, Brody ( Brody )",VI,C,brodmurp@haverford.org
"Ronon, Gerald ( Tripp )",VI,C,gerarono@haverford.org
"Rouse, John ( John )",VI,C,johnrous@haverford.org
"Seward, William ( Henry )",VI,C,willsewa@haverford.org
"Walker, William ( William )",VI,C,willwalk@haverford.org
"Watson, Luke ( Luke )",VI,C,lukewats@haverford.org
"Williams, Casey ( Casey )",VI,C,casewill@haverford.org
"Yoh, Russell ( Russell )",VI,C,russyoh@haverford.org
"Zhang, Max ( Max )",VI,C,maxzhan@haverford.org
"Jones, Matthew ( Matt )",IV,D,mattjone@haverford.org
"Bonner, Declan ( Declan )",V,D,declbonn@haverford.org
"Carpenter, Devin ( Devin )",V,D,devicarp@haverford.org
"Cloran, Duke ( Duke )",V,D,dukeclor@haverford.org
"Cohen, Patrick ( Pat )",V,D,patrcohe@haverford.org
"Cooper, Gavin ( Gavin )",V,D,gavicoop@haverford.org
"Dalton, Connor ( Connor )",V,D,conndalt@haverford.org
"Degenhardt, Kai ( Kai )",V,D,kaidege@haverford.org
"Fertels, Maxwell ( Max )",V,D,maxwfert@haverford.org
"Gaffney, Thomas ( Mac )",V,D,thomgaff@haverford.org
"Gord, Charles ( Charlie )",V,D,chargord@haverford.org
"Haney, Connor ( Connor )",V,D,connhane@haverford.org
"Haron, Myles ( Myles )",V,D,myleharo@haverford.org
"Jones, Preston ( Preston )",V,D,presjone@haverford.org
"Kanchwala, Abdullah ( Abdullah )",V,D,abdukanc@haverford.org
"Kanefsky, Noah ( Noah )",V,D,noahkane@haverford.org
"Li, Devon ( Devon )",V,D,devoli@haverford.org
"Manogue, Phineas ( Phineas )",V,D,phinmano@haverford.org
"Meyer, Griffin ( Griffin )",V,D,grifmeye@haverford.org
"Millard, Mason ( Mason )",V,D,masomill@haverford.org
"Noble, Charles ( Charlie )",V,D,charnobl@haverford.org
"Patterson, Christos ( Christos )",V,D,chripatt@haverford.org
"Rogers, Jay (Jay )",V,D,jayroge@haverford.org
"Saial, Ali ( Ali )",V,D,alisaia@haverford.org
"Saul, Thomas ( Tommy )",V,D,thomsaul@haverford.org
"Simpkins, Connor ( Connor )",V,D,connsimp@haverford.org
"Smith, Cameron ( Cameron )",V,D,camesmit@haverford.org
"Williams, Joshua ( Josh )",V,D,joshwill@haverford.org
"Yerger, Matthew ( Matthew )",V,D,mattyerg@haverford.org
"Andrewson, Noah ( Noah )",VI,D,noahandr@haverford.org
"Bonaparte, Jai ( Jai )",VI,D,jaibona@haverford.org
"Cuddeback, John ( Jack )",VI,D,johncudd@haverford.org
"Gillespie, Connor ( Connor )",VI,D,conngill@haverford.org
"Herbert, Graeme ( Graeme )",VI,D,graeherb@haverford.org
"Jones, Matthew ( Matty )",VI,D,mattjone@haverford.org
"Kahana, Nathan ( Nathan )",VI,D,nathkaha@haverford.org
"Keidel, Philip ( Charlie )",VI,D,philkeid@haverford.org
"Long, Jackson ( Jack )",VI,D,jacklong@haverford.org
"O'Kane, Brady ( Brady )",VI,D,brado'ka@haverford.org
"Rayer, William ( Billy )",VI,D,willraye@haverford.org
"Smith, Holden ( Holden )",VI,D,holdsmit@haverford.org
"Stamps, Gavin ( Gavin )",VI,D,gavistam@haverford.org
"Stewart, David ( David )",VI,D,davistew@haverford.org
"Vogel, Tanner ( Tanner )",VI,D,tannvoge@haverford.org
"Wu, Preston ( Preston )",VI,D,preswu@haverford.org
"Bartholdson, Michael ( Michael )",V,E,michbart@haverford.org
"Brown, Harrison ( Harrison )",V,E,harrbrow@haverford.org
"Busser, Robert ( Robby )",V,E,robebuss@haverford.org
"Crowder, Gabriel ( Gabriel )",V,E,gabrcrow@haverford.org
"Esposito, Cameron ( Cameron )",V,E,cameespo@haverford.org
"Gaffney, Thomas ( Mac )",V,E,thomgaff@haverford.org
"Matuch, Alexander ( Xan )",V,E,alexmatu@haverford.org
"White, Patrick ( Patrick )",V,E,patrwhit@haverford.org
"Belden, Daniel ( Daniel )",VI,E,danibeld@haverford.org
"Bongiovanni, Joseph ( Quin )",VI,E,josebong@haverford.org
"Bowers, Quintin ( Quintin )",VI,E,quinbowe@haverford.org
"Cerniglia, Robert ( Robert )",VI,E,robecern@haverford.org
"DiRocco, Aydan ( Aydan )",VI,E,aydadiro@haverford.org
"Gibson, Edward ( Edward )",VI,E,edwagibs@haverford.org
"Gildea, Thomas (Tom )",VI,E,thomgild@haverford.org
"Green, William ( Clayton )",VI,E,willgree@haverford.org
"Gross, Adon ( Adon )",VI,E,adongros@haverford.org
"Harrington, Jackson ( Jackson )",VI,E,jackharr@haverford.org
"Herd, Joseph ( Joseph )",VI,E,joseherd@haverford.org
"Inniss, Andre ( Andre )",VI,E,andrinni@haverford.org
"Jiru, Samuel ( Samuel )",VI,E,samujiru@haverford.org
"Kaplan, Thomas ( Thomas )",VI,E,thomkapl@haverford.org
"Kriebel, Garrett ( Garrett )",VI,E,garrkrie@haverford.org
"Lawrence, Peter ( Finn )",VI,E,petelawr@haverford.org
"Lee, Ethan ( Ethan )",VI,E,ethalee@haverford.org
"McCloskey, Nolan ( Nolan )",VI,E,nolamccl@haverford.org
"Miles, Michael ( Brady )",VI,E,michmile@haverford.org
"Nemo, Alexander ( Alex )",VI,E,alexnemo@haverford.org
"Ngo, Sean ( Sean )",VI,E,seanngo@haverford.org
"Paul, Blake ( Blake )",VI,E,blakpaul@haverford.org
"Popky, Robert ( Bobby )",VI,E,robepopk@haverford.org
"Pryma, Reilly ( Reilly )",VI,E,reilprym@haverford.org
"Rosenberger, Anthony ( A.J.)",VI,E,anthrose@haverford.org
"Scanlan, Connor ( Connor )",VI,E,connscan@haverford.org
"Valentino, Anthony ( Anthony )",VI,E,anthvale@haverford.org
"Young, Banks ( Banks )",VI,E,bankyoun@haverford.org
"Brodnik, Timothy ( TJ )",IV,F,timobrod@haverford.org
"Andrewson, Noah ( Noah )",VI,F,noahandr@haverford.org
"Bradley, Andrew ( Andrew )",VI,F,andrbrad@haverford.org
"Brodnik, Sean ( Sean )",VI,F,seanbrod@haverford.org
"Burfeind, William ( Will )",VI,F,willburf@haverford.org
"Cresswell, Connor ( Connor )",VI,F,conncres@haverford.org
"Etherington, Lowen ( Lowen )",VI,F,loweethe@haverford.org
"Fan, Justin ( Justin )",VI,F,justfan@haverford.org
"Feigenberg, Matthew ( Matthew )",VI,F,mattfeig@haverford.org
"Fesnak, Luke ( Luke )",VI,F,lukefesn@haverford.org
"Ford, Render ( Render )",VI,F,rendford@haverford.org
"Glaser, Andrew ( Drew )",VI,F,andrglas@haverford.org
"Golderer, Sebastian ( Sebastian )",VI,F,sebagold@haverford.org
"Green, William ( Clayton )",VI,F,willgree@haverford.org
"Gross, Adon ( Adon )",VI,F,adongros@haverford.org
"Kaiser, Daniel ( Daniel )",VI,F,danikais@haverford.org
"Long, Jackson ( Jack )",VI,F,jacklong@haverford.org
"Nelson, Chase ( Chase )",VI,F,chasnels@haverford.org
"Putter, Lucas ( Luke )",VI,F,lucaputt@haverford.org
"Shaffer, Reilly ( Reilly )",VI,F,reilshaf@haverford.org
"Shatzman, Chase ( Chase )",VI,F,chasshat@haverford.org
"Trexler, Noah ( Noah )",VI,F,noahtrex@haverford.org
"White, Michael ( Ian )",VI,F,michwhit@haverford.org
"Williams, Casey ( Casey )",VI,F,casewill@haverford.org
"Wolitarsky, James ( William )",VI,F,jamewoli@haverford.org
"Harvison, Harvey ( Harvey )",V,G,harvharr@haverford.org
"Peshek-Percec, Alexander ( Alexander )",VI,G,alexpesh@haverford.org
"Harvison, Harvey ( Harvey )",V,G,harvharv@haverford.org
"Reavey, Kevin ( Kevin )",VI,G,kevireav@haverford.org
"Baker, Gabriel ( Gabriel )",V,G,gabrbake@haverford.org
"Stallkamp, Brady ( Brady )",VI,G,bradstal@haverford.org
"Benson, Grey ( Grey )",V,G,greybens@haverford.org
"Block, Brandon ( Brandon )",V,G,branbloc@haverford.org
"Bonaparte, Aaron ( Aaron )",V,G,aarobona@haverford.org
"Boratto, Evan ( Evan )",V,G,evanbora@haverford.org
"Borden, Andrew ( Andrew )",V,G,andrbord@haverford.org
"Burman, Nathaniel ( Nate )",V,G,nathburm@haverford.org
"Covington, Kevin ( Kevin )",V,G,kevicovi@haverford.org
"Dardarian, Alexander ( Alexander )",V,G,alexdard@haverford.org
"Dombar, Simon ( Simon )",V,G,simodomb@haverford.org
"Duska, Ronald ( Miguel )",V,G,ronadusk@haverford.org
"Erskine, Benjamin ( Ben )",V,G,benjersk@haverford.org
"Farrington, Ethan ( Ethan )",V,G,ethafarr@haverford.org
"Fuscaldo, Zachary ( Zachary )",V,G,zachfusc@haverford.org
"Gergo, Peter ( Peter )",V,G,petegerg@haverford.org
"Goens, Robert ( Robert )",V,G,robegoen@haverford.org
"Halpert, Charles ( Charlie )",V,G,charhalp@haverford.org
"Hoban, Joseph ( JP )",V,G,josehoba@haverford.org
"Hope, Reilly ( Reilly )",V,G,reilhope@haverford.org
"Johnson, Amir ( Amir )",V,G,amirjohn@haverford.org
"Jones, Avery ( Avery )",V,G,averjone@haverford.org
"Krey, Alexander ( Alex )",V,G,alexkrey@haverford.org
"Leader, Elijah ( Eli)",V,G,elijlead@haverford.org
"Lu, Nicholas ( Nicholas )",V,G,nichlu@haverford.org
"McClave, Jude ( Jude )",V,G,judemccl@haverford.org
"Pennewill, David ( DJ )",V,G,davipenn@haverford.org
"Rhodes, Alexander ( Alex )",V,G,alexrhod@haverford.org
"Romero, Thomas ( TJ )",V,G,thomrome@haverford.org
"Sharma, Unnav ( Unnav )",V,G,unnashar@haverford.org
"Stait, Jamie ( Jamie )",V,G,jamistai@haverford.org
"Swei, Preston ( Preston )",V,G,presswei@haverford.org
"Tierney, Finnegan ( Finn )",V,G,finntier@haverford.org
"Waters, Kwamen ( Kwamen )",V,G,kwamwate@haverford.org
"Weissenberger, Gregor ( Gregor )",V,G,gregweis@haverford.org
"Wiedmer, Alistair ( Alistair )",V,G,aliswied@haverford.org
"Aggarwal, Arsh ( Arsh )",VI,G,arshagga@haverford.org
"Baker, Dawson ( Dawson )",VI,G,dawsbake@haverford.org
"Barnes-Pace, Michael ( Mick )",VI,G,michbarn@haverford.org
"Brewington, Ryan ( Ryan )",VI,G,ryanbrew@haverford.org
"Brodnik, Sean ( Sean )",VI,G,seanbrod@haverford.org
"Carter, Anthony ( Anthony )",VI,G,anthcart@haverford.org
"Colsher, Ryan ( Ryan )",VI,G,ryancols@haverford.org
"Gates, James ( James )",VI,G,jamegate@haverford.org
"Hengst, Austan ( Austan )",VI,G,austheng@haverford.org
"Jacobs, Keegan ( Keegan )",VI,G,keegjaco@haverford.org
"Laveran, Pierce ( Pierce )",VI,G,pierlave@haverford.org
"Marr, Maximillian ( Max )",VI,G,maximarr@haverford.org
"Mignucci, Nicholas ( Nicholas )",VI,G,nichmign@haverford.org
"Nayak, Adiyan ( Adi )",VI,G,adiynaya@haverford.org
"Nolen, Connor ( Connor )",VI,G,connnole@haverford.org
"Winikur, Asa ( Asa )",VI,G,asawini@haverford.org
"Wolitarsky, James ( William )",VI,G,jamewoli@haverford.org
"Newhall, Henry ( Henry )",VI,G,henrnewh@haverford.org"""

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