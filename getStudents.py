import csv

# Returns the list of students who have the given free period first

class Student:
    def __init__(self, grade, email, signedIn=False):
        self.grade = grade
        self.signedIn = signedIn
        self.email = email

def getStudents(period):
    students = {}
    nameIndex = 1
    gradeIndex = 2
    periodIndex = 3
    emailIndex = 4

    # CSV data as a multi-line string
    csv_data = """ID,name,grade,free,email
    COOP051,"Cooper, Gavin ( Gavin )",IV,A,gavicoop@haverford.org
    GERG011,"Gergo, Peter ( Peter )",IV,A,petegerg@haverford.org
    BONA011,"Bonaparte, Jai ( Jai )",V,A,jaibona@haverford.org
    GIBS021,"Gibson, Edward ( Edward )",V,A,edwagibs@haverford.org
    GREE131,"Green, William ( Clayton )",V,A,willgree@haverford.org
    GROS031,"Gross, Adon ( Adon )",V,A,adongros@haverford.org
    HARR061,"Harrington, Jackson ( Jackson )",V,A,jackharr@haverford.org
    INNI011,"Inniss, Andre ( Andre )",V,A,andrinni@haverford.org
    MILE011,"Miles, Michael ( Brady )",V,A,michmile@haverford.org
    MORA031,"Moran, Ryan ( Ryan )",V,A,ryanmora@haverford.org
    NELS041,"Nelson, Chase ( Chase )",V,A,chasnels@haverford.org
    NEMO011,"Nemo, Alexander ( Alex )",V,A,alexnemo@haverford.org
    NEWH012,"Newhall, Henry ( Henry )",V,A,henrnewh@haverford.org
    NOLE012,"Nolen, Connor ( Connor )",V,A,connnole@haverford.org
    PAUL031,"Paul, Blake ( Blake )",V,A,blakpaul@haverford.org
    PERE011,"Perez-Gasiba, Sebastian ( Sebastian )",V,A,sebapere@haverford.org
    PESH011,"Peshek-Percec, Alexander ( Alexander )",V,A,alexpesh@haverford.org
    RAYE011,"Rayer, William ( Billy )",V,A,willraye@haverford.org
    SHAF011,"Shaffer, Reilly ( Reilly )",V,A,reilshaf@haverford.org
    TREX011,"Trexler, Noah ( Noah )",V,A,noahtrex@haverford.org
    ZHAN031,"Zhang, Max ( Max )",V,A,maxzhan@haverford.org
    NYE011,"Nye, Thomas ( Thomas )",III,B,thomnye@haverford.org
    GAFF021,"Gaffney, Thomas ( Mac )",IV,B,thomgaff@haverford.org
    GILL081,"Gillis, Sebastian ( Sebastian )",IV,B,sebagill@haverford.org
    HALP012,"Halpert, Charles ( Charlie )",IV,B,charhalp@haverford.org
    LARG021,"Large, Evan ( Evan )",IV,B,evanlarg@haverford.org
    STAI011,"Stait, Jamie ( Jamie )",IV,B,jamistai@haverford.org
    ANDR041,"Andrewson, Noah ( Noah )",V,B,noahandr@haverford.org
    BROS012,"Brosko, Matthew ( Matt )",V,B,mattbros@haverford.org
    BROW171,"Brown, Jey ( Jey )",V,B,jeybrow@haverford.org
    BURF011,"Burfeind, William ( Will )",V,B,willburf@haverford.org
    CART031,"Carter, Anthony ( Anthony )",V,B,anthcart@haverford.org
    CIMI011,"Cimino, Richard ( Jack )",V,B,richcimi@haverford.org
    CONK011,"Conklin, Mitchell ( Tate )",V,B,mitcconk@haverford.org
    DELU011,"DeLuca, Alexander ( Alec )",V,B,alexdelu@haverford.org
    DUNB012,"Dunbar, Brandon ( Brandon )",V,B,brandunb@haverford.org
    FEIL011,"Feild, Dalton ( Dalton )",V,B,daltfeil@haverford.org
    FORD031,"Ford, Render ( Render )",V,B,rendford@haverford.org
    GILD011,"Gildea, Thomas ( Tom )",V,B,thomgild@haverford.org
    GOLD051,"Golderer, Sebastian ( Sebastian )",V,B,sebagold@haverford.org
    GROS031,"Gross, Adon ( Adon )",V,B,adongros@haverford.org
    HAYN011,"Hayne, Nicholas ( Nicholas )",V,B,nichhayn@haverford.org
    HERD022,"Herd, Joseph ( Joseph )",V,B,joseherd@haverford.org
    IBRA011,"Ibrahim, Amir ( Amir )",V,B,amiribra@haverford.org
    JACO032,"Jacobs, Keegan ( Keegan )",V,B,keegjaco@haverford.org
    JONE071,"Jones, Matthew ( Matty )",V,B,mattjone@haverford.org
    JONE141,"Jones-Blisard, Matthew ( Matthew )",V,B,mattjone@haverford.org
    KAPL042,"Kaplan, Thomas ( Thomas )",V,B,thomkapl@haverford.org
    KRIE011,"Kriebel, Garrett ( Garrett )",V,B,garrkrie@haverford.org
    LAWR021,"Lawrence, Peter ( Finn )",V,B,petelawr@haverford.org
    LEE081,"Lee, Ethan ( Ethan )",V,B,ethalee@haverford.org
    LYON031,"Lyon, Andrew ( Andrew )",V,B,andrlyon@haverford.org
    MARR011,"Marr, Maximillian ( Max )",V,B,maximarr@haverford.org
    MCCL032,"McCloskey, Nolan ( Nolan )",V,B,nolamccl@haverford.org
    MCCO071,"McCoy, John ( Thacher )",V,B,johnmcco@haverford.org
    MORR081,"Morris, Kyle ( Kyle )",V,B,kylemorr@haverford.org
    NAYA012,"Nayak, Adiyan ( Adi )",V,B,adiynaya@haverford.org
    NGO012,"Ngo, Sean ( Sean )",V,B,seanngo@haverford.org
    OKAN011,"O'Kane, Brady ( Brady )",V,B,bradokan@haverford.org
    PUTT011,"Putter, Lucas ( Luke )",V,B,lucaputt@haverford.org
    RALE012,"Raleigh, Jackson ( Jackson )",V,B,jackrale@haverford.org
    STAM022,"Stamps, Gavin ( Gavin )",V,B,gavistam@haverford.org
    VALE011,"Valentino, Anthony ( Anthony )",V,B,anthvale@haverford.org
    WINI013,"Winikur, Asa ( Asa )",V,B,asawini@haverford.org
    BAKE032,"Baker, Chase ( Chase )",III,C,chasbake@haverford.org
    CHAK022,"Chakraborty, Ajay ( AJ )",III,C,ajaychak@haverford.org
    CLAR061,"Clarke, Rauden ( Rauden )",III,C,raudclar@haverford.org
    CURR051,"Curran, Sean ( Sean )",III,C,seancurr@haverford.org
    DANI011,"Daniels, Luke ( Luke )",III,C,lukedani@haverford.org
    DANI021,"Danisi, Gabriel ( Gabe )",III,C,gabrdani@haverford.org
    DUVE011,"Duvernay, Lamar ( Lamar )",III,C,lamaduve@haverford.org
    FRAZ011,"Frazier, Walter ( Walt )",III,C,waltfraz@haverford.org
    GOIN021,"Goins, Ahijah ( Ahijah )",III,C,ahijgoin@haverford.org
    OLSO011,"Olson, Max ( Max )",III,C,maxolso@haverford.org
    PHIL021,"Phillips, Destin ( Destin )",III,C,destphil@haverford.org
    RISC011,"Rischitelli, John ( Jack )",III,C,johnrisc@haverford.org
    ROME031,"Romeo, Jovanni ( Jovanni )",III,C,jovarome@haverford.org
    ROUS011,"Rouse, Patrick ( Packy )",III,C,patrrous@haverford.org
    SHAM021,"Shams, Ryan ( Ryan )",III,C,ryansham@haverford.org
    TOTH011,"Toth, Colin ( Colin )",III,C,colitoth@haverford.org
    CUDD021,"Cuddeback, John ( Jack )",V,C,johncudd@haverford.org
    HENG011,"Hengst, Austan ( Austan )",V,C,austheng@haverford.org
    JABA011,"Jabateh, Musa ( Musa )",V,C,musajaba@haverford.org
    LAVE021,"Laveran, Pierce ( Pierce )",V,C,pierlave@haverford.org
    MCCA102,"McCarthy, Benjamin ( Ben )",V,C,benjmcca@haverford.org
    REAV011,"Reavey, Kevin ( Kevin )",V,C,kevireav@haverford.org
    RONO011,"Ronon, Gerald ( Tripp )",V,C,gerarono@haverford.org
    ROUS012,"Rouse, John ( John )",V,C,johnrous@haverford.org
    YOH022,"Yoh, Russell ( Russell )",V,C,russyoh@haverford.org
    CARR051,"Carrasco, Andrew ( Drew )",III,D,andrcarr@haverford.org
    GREE141,"Greenberg, Brady ( Brady )",III,D,bradgree@haverford.org
    HOBA012,"Hoban, Matthew ( Matt )",III,D,matthoba@haverford.org
    NEMO012,"Nemo, Nicholas ( Nicky )",III,D,nichnemo@haverford.org
    OLIV031,"Oliver, Grant ( Grant )",III,D,granoliv@haverford.org
    POWE051,"Powers, Maximilian ( Max )",III,D,maxipowe@haverford.org
    SHAN011,"Shannon, William ( Will )",III,D,willshan@haverford.org
    SIEV011,"Siever, Caleb ( Caleb )",III,D,calesiev@haverford.org
    SMYT021,"Smyth, Jaxen ( Jaxen )",III,D,jaxesmyt@haverford.org
    STIN031,"Stinchon, Oliver ( Oliver )",III,D,olivstin@haverford.org
    THOM131,"Thomas, Ian ( Ian )",III,D,ianthom@haverford.org
    DECK031,"Decker, Colin ( Colin )",IV,D,colideck@haverford.org
    KREY011,"Krey, Alexander ( Alex )",IV,D,alexkrey@haverford.org
    ROME021,"Romero, Thomas ( TJ )",IV,D,thomrome@haverford.org
    STOD011,"Stoddard, Ryan ( Ryan )",IV,D,ryanstod@haverford.org
    ANDR041,"Andrewson, Noah ( Noah )",V,D,noahandr@haverford.org
    CRES031,"Cresswell, Connor ( Connor )",V,D,conncres@haverford.org
    DIRO012,"DiRocco, Aydan ( Aydan )",V,D,aydadiro@haverford.org
    DUNB012,"Dunbar, Brandon ( Brandon )",V,D,brandunb@haverford.org
    FAN011,"Fan, Justin ( Justin )",V,D,justfan@haverford.org
    LONG041,"Long, Jackson ( Jack )",V,D,jacklong@haverford.org
    SCHW031,"Schwarting, Christopher ( Christopher )",V,D,chrischw@haverford.org
    WHIT111,"White, Michael ( Ian )",V,D,michwhit@haverford.org
    MCCL053,"McClave, Jude ( Jude )",IV,E,judemccl@haverford.org
    BARN071,"Barnes-Pace, Michael ( Mick )",V,E,michbarn@haverford.org
    BONG011,"Bongiovanni, Joseph ( Quin )",V,E,josebong@haverford.org
    BOWE031,"Bowers, Quintin ( Quintin )",V,E,quinbowe@haverford.org
    GLAS032,"Glaser, Andrew ( Drew )",V,E,andrglas@haverford.org
    HERB011,"Herbert, Graeme ( Graeme )",V,E,graeherb@haverford.org
    LYON031,"Lyon, Andrew ( Andrew )",V,E,andrlyon@haverford.org
    SHAT012,"Shatzman, Chase ( Chase )",V,E,chasshat@haverford.org
    VOGE011,"Vogel, Tanner ( Tanner )",V,E,tannvoge@haverford.org
    WALK062,"Walker, William ( William )",V,E,willwalk@haverford.org
    WU021,"Wu, Preston ( Preston )",V,E,preswu@haverford.org
    AGGA012,"Aggarwal, Arsh ( Arsh )",V,F,arshagga@haverford.org
    BELD011,"Belden, Daniel ( Daniel )",V,F,danibeld@haverford.org
    BRAD061,"Bradley, Andrew ( Andrew )",V,F,andrbrad@haverford.org
    BREW012,"Brewington, Ryan ( Ryan )",V,F,ryanbrew@haverford.org
    CERN011,"Cerniglia, Robert ( Robert )",V,F,robecern@haverford.org
    CRES031,"Cresswell, Connor ( Connor )",V,F,conncres@haverford.org
    ETHE011,"Etherington, Lowen ( Lowen )",V,F,loweethe@haverford.org
    FESN011,"Fesnak, Luke ( Luke )",V,F,lukefesn@haverford.org
    FORT021,"Forte, Jackson ( Jackson )",V,F,jackfort@haverford.org
    GATE011,"Gates, James ( James )",V,F,jamegate@haverford.org
    GILL061,"Gillespie, Connor ( Connor )",V,F,conngill@haverford.org
    HOYT013,"Hoyt, Benjamin ( Benjamin )",V,F,benjhoyt@haverford.org
    JIRU011,"Jiru, Samuel ( Samuel )",V,F,samujiru@haverford.org
    JORD011,"Jordan, Frederick ( Fred )",V,F,fredjord@haverford.org
    KAIS021,"Kaiser, Daniel ( Daniel )",V,F,danikais@haverford.org
    KEID011,"Keidel, Philip ( Charlie )",V,F,philkeid@haverford.org
    KOHL022,"Kohlenberg, John ( John )",V,F,johnkohl@haverford.org
    KOHN011,"Kohn, Edwin ( Eddie )",V,F,edwikohn@haverford.org
    MCCO051,"McComb, Benjamin ( Ben )",V,F,benjmcco@haverford.org
    MIGN012,"Mignucci, Nicholas ( Nicholas )",V,F,nichmign@haverford.org
    PRYM011,"Pryma, Reilly ( Reilly )",V,F,reilprym@haverford.org
    ROUS012,"Rouse, John ( John )",V,F,johnrous@haverford.org
    SEWA021,"Seward, William ( Henry )",V,F,willsewa@haverford.org
    SMIT151,"Smith, Holden ( Holden )",V,F,holdsmit@haverford.org
    STEW061,"Stewart, David ( David )",V,F,davistew@haverford.org
    WILL072,"Williams, Casey ( Casey )",V,F,casewill@haverford.org
    WOLI011,"Wolitarsky, James ( William )",V,F,jamewoli@haverford.org
    WYLI011,"Wylie, Michael ( Michael )",V,F,michwyli@haverford.org
    YOUN052,"Young, Banks ( Banks )",V,F,bankyoun@haverford.org
    CLOR023,"Cloran, Duke ( Duke )",IV,G,dukeclor@haverford.org
    DOMB011,"Dombar, Simon ( Simon )",IV,G,simodomb@haverford.org
    JONE072,"Jones, Preston ( Preston )",IV,G,presjone@haverford.org
    LEE101,"Lee, Semaj ( Semaj )",IV,G,semalee@haverford.org
    LU011,"Lu, Nicholas ( Nicholas )",IV,G,nichlu@haverford.org
    BAKE031,"Baker, Dawson ( Dawson )",V,G,dawsbake@haverford.org
    BART021,"Bartholdson, Anders ( Anders )",V,G,andebart@haverford.org
    BROD031,"Brodnik, Sean ( Sean )",V,G,seanbrod@haverford.org
    COLS011,"Colsher, Ryan ( Ryan )",V,G,ryancols@haverford.org
    CUDD021,"Cuddeback, John ( Jack )",V,G,johncudd@haverford.org
    FEIG011,"Feigenberg, Matthew ( Matthew )",V,G,mattfeig@haverford.org
    FORT021,"Forte, Jackson ( Jackson )",V,G,jackfort@haverford.org
    GLAS032,"Glaser, Andrew ( Drew )",V,G,andrglas@haverford.org
    KAHA011,"Kahana, Nathan ( Nathan )",V,G,nathkaha@haverford.org
    KELL081,"Kelly, William ( William )",V,G,willkell@haverford.org
    MCCA102,"McCarthy, Benjamin ( Ben )",V,G,benjmcca@haverford.org
    MCCO051,"McComb, Benjamin ( Ben )",V,G,benjmcco@haverford.org
    MURP021,"Murphy, Brody ( Brody )",V,G,brodmurp@haverford.org
    POPK011,"Popky, Robert ( Bobby )",V,G,robepopk@haverford.org
    ROSE072,"Rosenberger, Anthony ( A.J. )",V,G,anthrose@haverford.org
    SCAN011,"Scanlan, Connor ( Connor )",V,G,connscan@haverford.org
    STAL031,"Stallkamp, Brady ( Brady )",V,G,bradstal@haverford.org
    WATS041,"Watson, Luke ( Luke )",V,G,lukewats@haverford.org"""

    # creating a csv reader object from the multi-line string
    csvreader = csv.reader(csv_data.split('\n'))

    # extracting field names through first row,
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        free = row[periodIndex]
        if free == period:
            name = row[nameIndex]
            grade = row[gradeIndex]
            email = row[emailIndex]

            #students[name] = Student(grade,email)
            students[name] = {"signedIn": False, "grade": grade, "email": email,}

    return students
