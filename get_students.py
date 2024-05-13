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
    # should include all fifth (and for most of the year sixth) formers
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
"Campbell-Williams, Colin ( Colin )",V,A,colicamp@haverford.org
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
"White, Patrick ( Patrick )",V,C,patrwhit@haverford.org
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
"Bartholdson, Michael ( Michael )",V,E,michbart@haverford.org
"Brown, Harrison ( Harrison )",V,E,harrbrow@haverford.org
"Busser, Robert ( Robby )",V,E,robebuss@haverford.org
"Crowder, Gabriel ( Gabriel )",V,E,gabrcrow@haverford.org
"Esposito, Cameron ( Cameron )",V,E,cameespo@haverford.org
"Gaffney, Thomas ( Mac )",V,E,thomgaff@haverford.org
"Matuch, Alexander ( Xan )",V,E,alexmatu@haverford.org
"White, Patrick ( Patrick )",V,E,patrwhit@haverford.org
"Harvison, Harvey ( Harvey )",V,G,harvharr@haverford.org
"Harvison, Harvey ( Harvey )",V,G,harvharv@haverford.org
"Baker, Gabriel ( Gabriel )",V,G,gabrbake@haverford.org
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
"Wiedmer, Alistair ( Alistair )",V,G,aliswied@haverford.org"""

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
