from django.db import models

class Aircraft(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    fin = models.CharField(max_length=50, null=True)
    sea = models.BooleanField(default=False)
    tmg = models.BooleanField(default=False)
    efis = models.BooleanField(default=False)
    fnpt = models.IntegerField(null=True)
    make = models.CharField(max_length=100, null=True)
    run2 = models.BooleanField(default=False)
    _class = models.IntegerField(null=True)
    model = models.CharField(max_length=100, null=True)
    power = models.IntegerField(null=True)
    seats = models.IntegerField(null=True)
    active = models.BooleanField(default=False)
    kg5700 = models.BooleanField(default=False)
    rating = models.CharField(max_length=100, null=True)
    company = models.CharField(max_length=100, null=True)
    complex = models.BooleanField(default=False)
    condlog = models.IntegerField(null=True)
    engtype = models.IntegerField(null=True)
    favlist = models.BooleanField(default=False)
    category = models.IntegerField(null=True)
    enggroup = models.IntegerField(null=True)
    highperf = models.BooleanField(default=False)
    submodel = models.CharField(max_length=100, null=True)
    aerobatic = models.BooleanField(default=False)
    refsearch = models.CharField(max_length=100, null=True)
    reference = models.CharField(max_length=100, null=True)
    tailwheel = models.BooleanField(default=False)
    defaultapp = models.IntegerField(null=True)
    defaultlog = models.IntegerField(null=True)
    defaultops = models.IntegerField(null=True)
    devicecode = models.IntegerField(null=True)
    aircraftcode = models.UUIDField(unique=True)
    defaultlaunch = models.IntegerField(null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.make} {self.model} - {self.reference}"
    

class Pilot(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    notes = models.TextField(null=True)
    active = models.BooleanField(default=False)
    company = models.CharField(max_length=100, null=True)
    favlist = models.BooleanField(default=False)
    userapi = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    linkedin = models.CharField(max_length=255, null=True)
    pilotref = models.CharField(max_length=255, null=True)
    pilotcode = models.UUIDField()
    pilotname = models.CharField(max_length=100, null=True)
    pilotemail = models.EmailField(null=True)
    pilotphone = models.CharField(max_length=15, null=True)
    certificate = models.CharField(max_length=255, null=True)
    phonesearch = models.CharField(max_length=100, null=True)
    pilotsearch = models.CharField(max_length=255, null=True)
    rosteralias = models.CharField(max_length=255, null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return self.pilotname


class Flight(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    pf = models.BooleanField(default=False)
    pax = models.IntegerField(null=True)
    fuel = models.IntegerField(null=True)
    deice = models.BooleanField(default=False)
    cargo = models.IntegerField(null=True)
    route = models.CharField(max_length=255, null=True)
    today = models.IntegerField(null=True)
    minu1 = models.IntegerField(null=True)
    minu2 = models.IntegerField(null=True)
    minu3 = models.IntegerField(null=True)
    minu4 = models.IntegerField(null=True)
    minxc = models.IntegerField(null=True)
    arrrwy = models.CharField(max_length=100, null=True)
    deprwy = models.CharField(max_length=100, null=True)
    ldgday = models.IntegerField(null=True)
    liftsw = models.IntegerField(null=True)
    p1code = models.UUIDField()
    p2code = models.UUIDField()
    p3code = models.UUIDField()
    p4code = models.UUIDField()
    report = models.TextField(null=True)
    tagops = models.CharField(max_length=100, null=True)
    toedit = models.BooleanField(default=False)
    minair = models.IntegerField(null=True)
    mincop = models.IntegerField(null=True)
    minifr = models.IntegerField(null=True)
    minimt = models.IntegerField(null=True)
    minpic = models.IntegerField(null=True)
    minrel = models.IntegerField(null=True)
    minsfr = models.IntegerField(null=True)
    arrcode = models.UUIDField()
    dateutc = models.DateField(null=True)
    depcode = models.UUIDField()
    hobbsin = models.IntegerField(null=True)
    holding = models.IntegerField(null=True)
    pairing = models.CharField(max_length=100, null=True)
    remarks = models.TextField(null=True)
    signbox = models.IntegerField(null=True)
    tonight = models.IntegerField(null=True)
    usernum = models.IntegerField(null=True)
    mindual = models.IntegerField(null=True)
    minexam = models.IntegerField(null=True)
    crewlist = models.CharField(max_length=255, null=True)
    datebase = models.DateField(null=True)
    fuelused = models.IntegerField(null=True)
    hobbsout = models.IntegerField(null=True)
    ldgnight = models.IntegerField(null=True)
    nextpage = models.BooleanField(default=False)
    tagdelay = models.CharField(max_length=100, null=True)
    training = models.CharField(max_length=100, null=True)
    userbool = models.BooleanField(default=False)
    usertext = models.CharField(max_length=255, null=True)
    mininstr = models.IntegerField(null=True)
    minnight = models.IntegerField(null=True)
    minpicus = models.IntegerField(null=True)
    mintotal = models.IntegerField(null=True)
    arroffset = models.IntegerField(null=True)
    datelocal = models.DateField(null=True)
    depoffset = models.IntegerField(null=True)
    taglaunch = models.CharField(max_length=100, null=True)
    taglesson = models.CharField(max_length=100, null=True)
    totimeutc = models.IntegerField(null=True)
    arrtimeutc = models.IntegerField(null=True)
    baseoffset = models.IntegerField(null=True)
    deptimeutc = models.IntegerField(null=True)
    flightcode = models.UUIDField()
    ldgtimeutc = models.IntegerField(null=True)
    fuelplanned = models.IntegerField(null=True)
    nextsummary = models.BooleanField(default=False)
    tagapproach = models.CharField(max_length=100, null=True)
    aircraftcode =models.CharField(max_length=255, null=True)
    arrtimesched = models.IntegerField(null=True)
    deptimesched = models.IntegerField(null=True)
    flightnumber = models.CharField(max_length=50, null=True)
    flightsearch = models.CharField(max_length=255, null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"Flight {self.flightnumber} on {self.dateutc}"


class SettingConfig(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    configcode = models.IntegerField(unique=True)
    data = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    group = models.CharField(max_length=255, null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}: {self.data}"


class Airfield(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    afcode = models.UUIDField(unique=True, null=True)
    afcat = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)
    affaa = models.CharField(max_length=100, null=True)
    notes = models.CharField(max_length=100, null=True)
    useredit = models.BooleanField(default=False)
    afiata = models.CharField(max_length=100, null=True)
    aficao = models.CharField(max_length=100, null=True)
    afname = models.CharField(max_length=255, null=True)
    tzcode = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    showlist = models.BooleanField(default=False)
    afcountry = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)
    notesuser = models.CharField(max_length=255, null=True)
    regionuser = models.IntegerField(null=True)
    elevationft = models.IntegerField(null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.guid}: {self.platform}"


class Imagepic(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    fileext = models.CharField(max_length=100, null=True)
    imgcode = models.UUIDField(unique=True)
    filename = models.CharField(max_length=255, null=True)
    linkcode = models.CharField(max_length=255, null=True)
    img_upload = models.BooleanField(default=False)
    img_download = models.BooleanField(default=False)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.filename}: {self.fileext}"


class LimitRules(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    lto = models.CharField(max_length=25, null=True)
    lfrom = models.CharField(max_length=25, null=True)
    ltype = models.IntegerField(null=True)
    lzone = models.IntegerField(null=True)
    lminutes = models.IntegerField(null=True)
    limitcode = models.UUIDField(unique=True)
    lperiodcode = models.IntegerField(null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.limitcode}: {self.lperiodcode}"


class myQuery(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    mqcode = models.UUIDField(unique=True)
    quickview = models.BooleanField(default=False)
    shortname = models.CharField(max_length=100, null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}: {self.mqcode}"


class myQueryBuild(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    build1 = models.CharField(max_length=255, null=True)
    build2 = models.IntegerField(null=True)
    build3 = models.IntegerField(null=True)
    build4 = models.CharField(max_length=255, null=True)
    mqcode = models.CharField(max_length=255, null=True)
    mqbcode = models.UUIDField(unique=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.build1}: {self.mqcode}"


class Qualification(models.Model):
    user_id = models.IntegerField(null=True)
    guid = models.UUIDField(unique=True, null=True)
    platform = models.IntegerField(null=True)
    _modified = models.IntegerField(null=True)
    qcode = models.UUIDField(unique=True)
    refextra = models.IntegerField(null=True)
    refmodel = models.CharField(max_length=100, null=True)
    validity = models.IntegerField(null=True)
    datevalid = models.CharField(max_length=100, null=True)
    qtypecode = models.IntegerField(null=True)
    dateissued = models.CharField(max_length=255, null=True)
    minimumqty = models.IntegerField(null=True)
    notifydays = models.IntegerField(null=True)
    refairfield = models.CharField(max_length=255, null=True)
    minimumperiod = models.IntegerField(null=True)
    notifycomment = models.CharField(max_length=255, null=True)
    record_modified = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.qcode}: {self.notifycomment}"
      