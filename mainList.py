#Webscrapping vagas Gupy

import requests, json, copy
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#extrator Guppy
def consultaVagas(companycode):
    print("################")
    print("CONSULTANDO COMPANY CODE: "+str(companycode))
    print("################")
    if companycode == 1:
        companyName = 'randon'
    elif companycode == 2:
        companyName = 'soprano'
    elif companycode == 3:
        companyName = 'promob'
    elif companycode == 4:
        companyName = 'totvs'
    elif companycode == 5:
        companyName = 'unicred'
    elif companycode == 6:
        companyName = 'renner'
    elif companycode == 7:
        companyName = 'sicredi'
    elif companycode == 8:
        companyName = 'grupobrinox'
    elif companycode == 9:
        companyName = 'pmweb'
    elif companycode == 10:
        companyName = 'martiplast'
    elif companycode == 11:
        companyName = 'megawork'
    elif companycode == 12:
        companyName = 'lamoda'
    elif companycode == 13:
        companyName = 'grupoboticario'
    elif companycode == 14:
        companyName = 'eletronor'
    elif companycode == 15:
        companyName = '4all'
    elif companycode == 16:
        companyName = 'ambevtech'
    elif companycode == 17:
        companyName = 'b2w'
    elif companycode == 18:
        companyName = 'braskem'
    elif companycode == 19:
        companyName = 'cielo'
    elif companycode == 20:
        companyName = 'econet'
    elif companycode == 21:
        companyName = 'eixosp'
    elif companycode == 22:
        companyName = 'eletronor'
    elif companycode == 23:
        companyName = "elo7"
    elif companycode == 24:
        companyName = "elogroup"
    elif companycode == 25:
        companyName = "elsons"
    elif companycode == 26: 
        companyName = "embracon"
    elif companycode == 27:
        companyName = "embraer"
    elif companycode == 28:
        companyName = "emcasa"
    elif companycode == 29:
        companyName = "endeavor"
    elif companycode == 30:
        companyName = "engepack"
    elif companycode == 31:
        companyName = "engiebrasilenergia"
    elif companycode == 32:
        companyName = "enjoei"
    elif companycode == 33:
        companyName = "entrevias"
    elif companycode == 34:
        companyName = "enxuto"
    elif companycode == 35:
        companyName = "epharma"
    elif companycode == 36:
        companyName = "esales"
    elif companycode == 37:
        companyName = "escolacamb"
    elif companycode == 38:
        companyName = "escolaeleva"
    elif companycode == 39:
        companyName = "escolamais"
    elif companycode == 40:
        companyName = "escolamoppe"
    elif companycode == 41:
        companyName = "esss"
    elif companycode == 42:
        companyName = "estantemagica"
    elif companycode == 43:
        companyName = "eurobike"
    elif companycode == 44:
        companyName = "eurofarma"
    elif companycode == 45:
        companyName = "everyti"
    elif companycode == 46:
        companyName = "evino"
    elif companycode == 47:
        companyName = "evow12"
    elif companycode == 48:
        companyName = "ewave"
    elif companycode == 49:
        companyName = "exactaworks"
    elif companycode == 50:
        companyName = "expressosaomiguel"
    elif companycode == 51:
        companyName = "extrafruti"
    elif companycode == 52:
        companyName = "facell"
    elif companycode == 53:
        companyName = "farmax"
    elif companycode == 54:
        companyName = "fattu"
    elif companycode == 55:
        companyName = "fbiz"
    elif companycode == 56:
        companyName = "fcjventurebuilder"
    elif companycode == 57:
        companyName = "fertilizantestocantins"
    elif companycode == 58:
        companyName = "festo"
    elif companycode == 59:
        companyName = "fidi"
    elif companycode == 60:
        companyName = "finx"
    elif companycode == 61:
        companyName = "flora"
    elif companycode == 62:
        companyName = "fnc"
    elif companycode == 63:
        companyName = "fococonsultancy"
    elif companycode == 64:companyName = "fortlev"
    elif companycode == 65:companyName = "friend"
    elif companycode == 66:companyName = "fsb"
    elif companycode == 67:companyName = "fujitsu"
    elif companycode == 68:companyName = "fundacao-lemann"
    elif companycode == 69:companyName = "fundahc"
    elif companycode == 70:companyName = "gal"
    elif companycode == 71:companyName = "gamersclub"
    elif companycode == 72:companyName = "gateware"
    elif companycode == 73:companyName = "gedorebrasil"
    elif companycode == 74:companyName = "gentilnegocios"
    elif companycode == 75:companyName = "gera"
    elif companycode == 76:companyName = "gerandofalcoes"
    elif companycode == 77:companyName = "gfbr"
    elif companycode == 78:companyName = "ghfly"
    elif companycode == 79:companyName = "gilbarco"
    elif companycode == 80:companyName = "gntech"
    elif companycode == 81:companyName = "golcarreiras"
    elif companycode == 82:companyName = "gp-investments"
    elif companycode == 83:companyName = "gpa"
    elif companycode == 84:companyName = "greatplacetowork"
    elif companycode == 85:companyName = "group1auto"
    elif companycode == 86:companyName = "grpcom"
    elif companycode == 87:companyName = "grupoboticario"
    elif companycode == 88:companyName = "grupobrinox"
    elif companycode == 89:companyName = "grupocetefe"
    elif companycode == 90:companyName = "grupocoringa"
    elif companycode == 91:companyName = "grupodaycoval"
    elif companycode == 92:companyName = "grupogaia"
    elif companycode == 93:companyName = "grupohennings"
    elif companycode == 94:companyName = "grupohinode"
    elif companycode == 95:companyName = "grupoindiana"
    elif companycode == 96:companyName = "grupoitss"
    elif companycode == 97:companyName = "grupolevel"
    elif companycode == 98:companyName = "grupomantiqueira"
    elif companycode == 99:companyName = "grupomater"
    elif companycode == 100:companyName = "grupomateus"
    elif companycode == 101:companyName = "grupomoura"
    elif companycode == 102:companyName = "gruponc"
    elif companycode == 103:companyName = "gruporaccoon"
    elif companycode == 104:companyName = "gruporb"
    elif companycode == 105:companyName = "gruporeal"
    elif companycode == 106:companyName = "gruporeferencial"
    elif companycode == 107:companyName = "gruporizatti"
    elif companycode == 108:companyName = "gruposa"
    elif companycode == 109:companyName = "gruposc"
    elif companycode == 110:companyName = "gruposeb"
    elif companycode == 111:companyName = "gruposertecrh"
    elif companycode == 112:companyName = "gruposervnac"
    elif companycode == 113:companyName = "gruposhbrasil"
    elif companycode == 114:companyName = "gruposinosserra"
    elif companycode == 115:companyName = "gruposoma"
    elif companycode == 116:companyName = "grupotrigo"
    elif companycode == 117:companyName = "grupouol"
    elif companycode == 118:companyName = "gscintegradora"
    elif companycode == 119:companyName = "guaridacarreiras"
    elif companycode == 120:companyName = "haoc"
    elif companycode == 121:companyName = "harald"
    elif companycode == 122:companyName = "havan"
    elif companycode == 123:companyName = "hbsis"
    elif companycode == 124:companyName = "hdiseguros"
    elif companycode == 125:companyName = "heads"
    elif companycode == 126:companyName = "heinz"
    elif companycode == 127:companyName = "helbor-hbr"
    elif companycode == 128:companyName = "helenarh"
    elif companycode == 129:companyName = "hetta"
    elif companycode == 130:companyName = "hidrovias"
    elif companycode == 131:companyName = "hiplatform"
    elif companycode == 132:companyName = "hitechnologies"
    elif companycode == 133:companyName = "hmengenharia"
    elif companycode == 134:companyName = "hnsn"
    elif companycode == 135:companyName = "hospitaldeamor"
    elif companycode == 136:companyName = "hostfiber"
    elif companycode == 137:companyName = "hostinger"
    elif companycode == 138:companyName = "hsinvest"
    elif companycode == 139:companyName = "hurb"
    elif companycode == 140:companyName = "hypera"
    elif companycode == 141:companyName = "icarotech"
    elif companycode == 142:companyName = "iclinic"
    elif companycode == 143:companyName = "ictransportes"
    elif companycode == 144:companyName = "ignicaodigital"
    elif companycode == 145:companyName = "iguacumaquinas"
    elif companycode == 146:companyName = "ilegra"
    elif companycode == 147:companyName = "ilhasoft"
    elif companycode == 148:companyName = "imerge"
    elif companycode == 149:companyName = "impactoprime"
    elif companycode == 150:companyName = "imtep"
    elif companycode == 151:companyName = "indra"
    elif companycode == 152:companyName = "inec"
    elif companycode == 153:companyName = "infoprice"
    elif companycode == 154:companyName = "ingaia"
    elif companycode == 155:companyName = "ingressocom"
    elif companycode == 156:companyName = "inlog"
    elif companycode == 157:companyName = "inmetrics"
    elif companycode == 158:companyName = "inmetricschile"
    elif companycode == 159:companyName = "inovationit"
    elif companycode == 160:companyName = "institutoayrtonsenna"
    elif companycode == 161:companyName = "integramedicina"
    elif companycode == 162:companyName = "investtools"
    elif companycode == 163:companyName = "invillia"
    elif companycode == 164:companyName = "ioasys"
    elif companycode == 165:companyName = "ipnet"
    elif companycode == 166:companyName = "ipog"
    elif companycode == 167:companyName = "isentrega"
    elif companycode == 168:companyName = "issbrasil"
    elif companycode == 169:companyName = "isystems"
    elif companycode == 170:companyName = "jadlog"
    elif companycode == 171:companyName = "james"
    elif companycode == 172:companyName = "japi"
    elif companycode == 173:companyName = "jasmine"
    elif companycode == 174:companyName = "jbs"
    elif companycode == 175:companyName = "jeffreygroupbrasil"
    elif companycode == 176:companyName = "jeitto"
    elif companycode == 177:companyName = "jesuitasbrasil"
    elif companycode == 178:companyName = "jointecnologia"
    elif companycode == 179:companyName = "jorgeto"
    elif companycode == 180:companyName = "juno"
    elif companycode == 181:companyName = "juntoseguros"
    elif companycode == 182:companyName = "juntossomosmais"
    elif companycode == 183:companyName = "jussi"
    elif companycode == 184:companyName = "karsten"
    elif companycode == 185:companyName = "klickpages"
    elif companycode == 186:companyName = "kobe"
    elif companycode == 187:companyName = "kovi"
    elif companycode == 188:companyName = "krones"
    elif companycode == 189:companyName = "kryptus"
    elif companycode == 190:companyName = "kumulus"
    elif companycode == 191:companyName = "labtest"
    elif companycode == 192:companyName = "lafs"
    elif companycode == 193:companyName = "lamoda"
    elif companycode == 194:companyName = "lanlink"
    elif companycode == 195:companyName = "lar-app"
    elif companycode == 196:companyName = "lasa"
    elif companycode == 197:companyName = "ldcelulose"
    elif companycode == 198:companyName = "leads2b"
    elif companycode == 199:companyName = "leega"
    elif companycode == 200:companyName = "levelgroup"
    elif companycode == 201:companyName = "libercapital"
    elif companycode == 202:companyName = "light"
    elif companycode == 203:companyName = "linea"
    elif companycode == 204:companyName = "linkapi"
    elif companycode == 205:companyName = "livelo"
    elif companycode == 206:companyName = "loccitane"
    elif companycode == 207:companyName = "loftdesign"
    elif companycode == 208:companyName = "loginlogistica"
    elif companycode == 209:companyName = "logosrh"
    elif companycode == 210:companyName = "lojasqueroquero"
    elif companycode == 211:companyName = "lojastenda"
    elif companycode == 212:companyName = "lopes"
    elif companycode == 213:companyName = "loud"
    elif companycode == 214:companyName = "m4u"
    elif companycode == 215:companyName = "machadomeyer"
    elif companycode == 216:companyName = "macroconnect"
    elif companycode == 217:companyName = "madeiracarreira"
    elif companycode == 218:companyName = "madesa"
    elif companycode == 219:companyName = "maisdiversidade"
    elif companycode == 220:companyName = "mamaquinas"
    elif companycode == 221:companyName = "maniadechurrasco"
    elif companycode == 222:companyName = "marisa"
    elif companycode == 223:companyName = "marisol"
    elif companycode == 224:companyName = "markup"
    elif companycode == 225:companyName = "martins"
    elif companycode == 226:companyName = "martiplast"
    elif companycode == 227:companyName = "matec"
    elif companycode == 228:companyName = "mattosfilho"
    elif companycode == 229:companyName = "maxmilhas"
    elif companycode == 230:companyName = "mbconsultoria"
    elif companycode == 231:companyName = "mblabs"
    elif companycode == 232:companyName = "medicamental"
    elif companycode == 233:companyName = "medway"
    elif companycode == 234:companyName = "megawork"
    elif companycode == 235:companyName = "memed"
    elif companycode == 236:companyName = "mendelics"
    elif companycode == 237:companyName = "mepoupe"
    elif companycode == 238:companyName = "mercadobitcoin"
    elif companycode == 239:companyName = "mercedes-benz"
    elif companycode == 240:companyName = "mercos"
    elif companycode == 241:companyName = "mideacarrier"
    elif companycode == 242:companyName = "mitrerealty"
    elif companycode == 243:companyName = "mlabs"
    elif companycode == 244:companyName = "monitoratec"
    elif companycode == 245:companyName = "montecarlo"
    elif companycode == 246:companyName = "movida"
    elif companycode == 247:companyName = "mrn"
    elif companycode == 248:companyName = "mtec"
    elif companycode == 249:companyName = "muffatovagas"
    elif companycode == 250:companyName = "mutantbrvagas"
    elif companycode == 251:companyName = "naturalone"
    elif companycode == 252:companyName = "nave-team"
    elif companycode == 253:companyName = "neomed"
    elif companycode == 254:companyName = "neshastore"
    elif companycode == 255:companyName = "netshowme"
    elif companycode == 256:companyName = "neuralmed"
    elif companycode == 257:companyName = "nexaresources"
    elif companycode == 258:companyName = "nexxera"
    elif companycode == 259:companyName = "nidec"
    elif companycode == 260:companyName = "nordresearch"
    elif companycode == 261:companyName = "norsul"
    elif companycode == 262:companyName = "nortox"
    elif companycode == 263:companyName = "novaescola"
    elif companycode == 264:companyName = "noverde"
    elif companycode == 265:companyName = "nts"
    elif companycode == 266:companyName = "numenit"
    elif companycode == 267:companyName = "nuvolax"
    elif companycode == 268:companyName = "nzn"
    elif companycode == 269:companyName = "oba"
    elif companycode == 270:companyName = "objective"
    elif companycode == 271:companyName = "ocyan"
    elif companycode == 272:companyName = "ohboy"
    elif companycode == 273:companyName = "oi"
    elif companycode == 274:companyName = "olambrasil"
    elif companycode == 275:companyName = "olist"
    elif companycode == 276:companyName = "omnibrasil"
    elif companycode == 277:companyName = "one"
    elif companycode == 278:companyName = "onizdistribuidora"
    elif companycode == 279:companyName = "onovolab"
    elif companycode == 280:companyName = "opportunity"
    elif companycode == 281:companyName = "orama"
    elif companycode == 282:companyName = "ourolac"
    elif companycode == 283:companyName = "p4engenharia"
    elif companycode == 284:companyName = "pagepersonnel"
    elif companycode == 285:companyName = "passeidireto"
    elif companycode == 286:companyName = "pemagri"
    elif companycode == 287:companyName = "peoplehr"
    elif companycode == 288:companyName = "perbras"
    elif companycode == 289:companyName = "petlove"
    elif companycode == 290:companyName = "petronas"
    elif companycode == 291:companyName = "petrorio"
    elif companycode == 292:companyName = "petros"
    elif companycode == 293:companyName = "pharlab"
    elif companycode == 294:companyName = "phonetrack"
    elif companycode == 295:companyName = "phosfaz"
    elif companycode == 296:companyName = "picpay"
    elif companycode == 297:companyName = "planoevendas"
    elif companycode == 298:companyName = "plenaalimentos"
    elif companycode == 299:companyName = "ploomes"
    elif companycode == 300:companyName = "pmweb"
    elif companycode == 301:companyName = "porte"
    elif companycode == 302:companyName = "positivo"
    elif companycode == 303:companyName = "potencialconsultoria"
    elif companycode == 304:companyName = "pradolux"
    elif companycode == 305:companyName = "pragma"
    elif companycode == 306:companyName = "pride"
    elif companycode == 307:companyName = "primeit"
    elif companycode == 308:companyName = "printi"
    elif companycode == 309:companyName = "privalia"
    elif companycode == 310:companyName = "projuris"
    elif companycode == 311:companyName = "promob"
    elif companycode == 312:companyName = "pronali"
    elif companycode == 313:companyName = "pulsus"
    elif companycode == 314:companyName = "qualidados"
    elif companycode == 315:companyName = "quantaprevidencia"
    elif companycode == 316:companyName = "queimadiaria"
    elif companycode == 317:companyName = "radix"
    elif companycode == 318:companyName = "raizen"
    elif companycode == 319:companyName = "randon"
    elif companycode == 320:companyName = "rankmyapp"
    elif companycode == 321:companyName = "realcafe"
    elif companycode == 322:companyName = "realprotect"
    elif companycode == 323:companyName = "rechagricola"
    elif companycode == 324:companyName = "redballoon"
    elif companycode == 325:companyName = "rededamas"
    elif companycode == 326:companyName = "redemoura"
    elif companycode == 327:companyName = "renner"
    elif companycode == 328:companyName = "rensz"
    elif companycode == 329:companyName = "repassa"
    elif companycode == 330:companyName = "revelo"
    elif companycode == 331:companyName = "rheaction"
    elif companycode == 332:companyName = "rhuni"
    elif companycode == 333:companyName = "ribercred"
    elif companycode == 334:companyName = "rinnai"
    elif companycode == 335:companyName = "risasa"
    elif companycode == 336:companyName = "picpay"
    elif companycode == 337:companyName = "rottas"
    elif companycode == 338:companyName = "rtf"
    elif companycode == 339:companyName = "ruralbrasil"
    elif companycode == 340:companyName = "s3saude"
    elif companycode == 341:companyName = "sami"
    elif companycode == 342:companyName = "sankhya"
    elif companycode == 343:companyName = "santacolomba"
    elif companycode == 344:companyName = "santahelena"
    elif companycode == 345:companyName = "santanderbrasil"
    elif companycode == 346:companyName = "santosbrasil"
    elif companycode == 347:companyName = "saocarlossaudeoncologica"
    elif companycode == 348:companyName = "saphyr"
    elif companycode == 349:companyName = "saqueepague"
    elif companycode == 350:companyName = "sauer"
    elif companycode == 351:companyName = "sbt"
    elif companycode == 352:companyName = "scania"
    elif companycode == 353:companyName = "schumann"
    elif companycode == 354:companyName = "sejadigna"
    elif companycode == 355:companyName = "sejaelgin"
    elif companycode == 356:companyName = "sejaitix"
    elif companycode == 357:companyName = "semantix"
    elif companycode == 358:companyName = "sepromotora"
    elif companycode == 359:companyName = "serasa"
    elif companycode == 360:companyName = "seredeconecta"
    elif companycode == 361:companyName = "serhum"
    elif companycode == 362:companyName = "serhumrh"
    elif companycode == 363:companyName = "serilon"
    elif companycode == 364:companyName = "servopa"
    elif companycode == 365:companyName = "sharecare"
    elif companycode == 366:companyName = "shopper"
    elif companycode == 367:companyName = "shoulder"
    elif companycode == 368:companyName = "sicoobmaxicredito"
    elif companycode == 369:companyName = "sicoobsul"
    elif companycode == 370:companyName = "sicredi"
    elif companycode == 371:companyName = "sidi"
    elif companycode == 372:companyName = "simpaul"
    elif companycode == 373:companyName = "slcagricola"
    elif companycode == 374:companyName = "slcmaquinas"
    elif companycode == 375:companyName = "smarapd"
    elif companycode == 376:companyName = "smarkio"
    elif companycode == 377:companyName = "smartbank"
    elif companycode == 378:companyName = "smilink"
    elif companycode == 379:companyName = "smlbrasil"
    elif companycode == 380:companyName = "sodexobeneficios"
    elif companycode == 381:companyName = "sodexoservicos"
    elif companycode == 382:companyName = "softdesign"
    elif companycode == 383:companyName = "solarcocacola"
    elif companycode == 384:companyName = "sollobrasil"
    elif companycode == 385:companyName = "solutis"
    elif companycode == 386:companyName = "solvimm"
    elif companycode == 387:companyName = "somosglobal"
    elif companycode == 388:companyName = "somosinova"
    elif companycode == 389:companyName = "somoslaguapa"
    elif companycode == 390:companyName = "soprano"
    elif companycode == 391:companyName = "soulconect"
    elif companycode == 392:companyName = "soultrade"
    elif companycode == 393:companyName = "soutocorrea"
    elif companycode == 394:companyName = "spark"
    elif companycode == 395:companyName = "spassu"
    elif companycode == 396:companyName = "spdm"
    elif companycode == 397:companyName = "spdmpais"
    elif companycode == 398:companyName = "spinpay"
    elif companycode == 399:companyName = "ssab"
    elif companycode == 400:companyName = "stb"
    elif companycode == 401:companyName = "studiosol"
    elif companycode == 402:companyName = "sumicity"
    elif companycode == 403:companyName = "supergasbras"
    elif companycode == 404:companyName = "superlogica"
    elif companycode == 405:companyName = "syncrh"
    elif companycode == 406:companyName = "t4f"
    elif companycode == 407:companyName = "tacchini"
    elif companycode == 408:companyName = "taglivros"
    elif companycode == 409:companyName = "talentgp"
    elif companycode == 410:companyName = "targetsistemas"
    elif companycode == 411:companyName = "tecban"
    elif companycode == 412:companyName = "techne"
    elif companycode == 413:companyName = "tecnobank"
    elif companycode == 414:companyName = "tecnofit"
    elif companycode == 415:companyName = "tecverde"
    elif companycode == 416:companyName = "tegraincorporadora"
    elif companycode == 417:companyName = "telefonicaed"
    elif companycode == 418:companyName = "telemont"
    elif companycode == 419:companyName = "tembici"
    elif companycode == 420:companyName = "terral"
    elif companycode == 421:companyName = "testcognisess"
    elif companycode == 422:companyName = "thbgroup"
    elif companycode == 423:companyName = "thenextbigfin"
    elif companycode == 424:companyName = "thinkseg"
    elif companycode == 425:companyName = "tigre"
    elif companycode == 426:companyName = "timacagro"
    elif companycode == 427:companyName = "time-now"
    elif companycode == 428:companyName = "tirolez"
    elif companycode == 429:companyName = "tiscoski"
    elif companycode == 430:companyName = "tit"
    elif companycode == 431:companyName = "tmsa"
    elif companycode == 432:companyName = "tokenlab"
    elif companycode == 433:companyName = "toledobrasil"
    elif companycode == 434:companyName = "toptaylor"
    elif companycode == 435:companyName = "toquefale"
    elif companycode == 436:companyName = "totvs"
    elif companycode == 437:companyName = "tpc"
    elif companycode == 438:companyName = "trabalhe-na-alemanha"
    elif companycode == 439:companyName = "trabalhenaace"
    elif companycode == 440:companyName = "trabalhenacesari"
    elif companycode == 441:companyName = "tree"
    elif companycode == 442:companyName = "trinusco"
    elif companycode == 443:companyName = "triples"
    elif companycode == 444:companyName = "trocafone"
    elif companycode == 445:companyName = "trybe"
    elif companycode == 446:companyName = "tunts"
    elif companycode == 447:companyName = "uatt"
    elif companycode == 448:companyName = "uberlandiarefrescos"
    elif companycode == 449:companyName = "ubyfol"
    elif companycode == 450:companyName = "uffa"
    elif companycode == 451:companyName = "unicesumar"
    elif companycode == 452:companyName = "unicred"
    elif companycode == 453:companyName = "unifeob"
    elif companycode == 454:companyName = "unilider"
    elif companycode == 455:companyName = "unimedbelem"
    elif companycode == 456:companyName = "unimedfortaleza"
    elif companycode == 457:companyName = "unimedjf"
    elif companycode == 458:companyName = "unimedpoa"
    elif companycode == 459:companyName = "urbitec"
    elif companycode == 460:companyName = "usaflex"
    elif companycode == 461:companyName = "useargo"
    elif companycode == 462:companyName = "usinasantaadelia"
    elif companycode == 463:companyName = "v4company"
    elif companycode == 464:companyName = "v8consulting"
    elif companycode == 465:companyName = "vale-verde"
    elif companycode == 466:companyName = "valecard"
    elif companycode == 467:companyName = "valid"
    elif companycode == 468:companyName = "velt"
    elif companycode == 469:companyName = "vempra"
    elif companycode == 470:companyName = "vempraahgora"
    elif companycode == 471:companyName = "vemprablu"
    elif companycode == 472:companyName = "vempradextra"
    elif companycode == 473:companyName = "vemprait4us"
    elif companycode == 474:companyName = "vempramc"
    elif companycode == 475:companyName = "vemprasciensa"
    elif companycode == 476:companyName = "vemprasofist"
    elif companycode == 477:companyName = "vemproibope"
    elif companycode == 478:companyName = "vemprolabi"
    elif companycode == 479:companyName = "vempropecege"
    elif companycode == 480:companyName = "vemsercomexport"
    elif companycode == 481:companyName = "vemsergran"
    elif companycode == 482:companyName = "vemsergrupogagliardi"
    elif companycode == 483:companyName = "vemserigua"
    elif companycode == 484:companyName = "vemserloures"
    elif companycode == 485:companyName = "vemsertechfit"
    elif companycode == 486:companyName = "vemserwill"
    elif companycode == 487:companyName = "verdesvales"
    elif companycode == 488:companyName = "vereda"
    elif companycode == 489:companyName = "vertem"
    elif companycode == 490:companyName = "vetta"
    elif companycode == 491:companyName = "vhsys"
    elif companycode == 492:companyName = "viacerta"
    elif companycode == 493:companyName = "viaflow"
    elif companycode == 494:companyName = "viavarejo"
    elif companycode == 495:companyName = "vibetecnologia"
    elif companycode == 496:companyName = "vibra"
    elif companycode == 497:companyName = "vincipartners"
    elif companycode == 498:companyName = "vindi"
    elif companycode == 499:companyName = "vivo"
    elif companycode == 500:companyName = "viziaoptica"
    elif companycode == 501:companyName = "vlmadv"
    elif companycode == 502:companyName = "voeazul"
    elif companycode == 503:companyName = "vortigo"
    elif companycode == 504:companyName = "votorantimcimentos"
    elif companycode == 505:companyName = "voxeldigital"
    elif companycode == 506:companyName = "warren"
    elif companycode == 507:companyName = "wayra-brasil"
    elif companycode == 508:companyName = "wbg"
    elif companycode == 509:companyName = "wbrain"
    elif companycode == 510:companyName = "webbytelecom"
    elif companycode == 511:companyName = "webmotors"
    elif companycode == 512:companyName = "weclever"
    elif companycode == 513:companyName = "werecruiter"
    elif companycode == 514:companyName = "westconcomstor-la"
    elif companycode == 515:companyName = "westwing"
    elif companycode == 516:companyName = "wheaton"
    elif companycode == 517:companyName = "whirlpool"
    elif companycode == 518:companyName = "wilsonsons"
    elif companycode == 519:companyName = "wine"
    elif companycode == 520:companyName = "winover"
    elif companycode == 521:companyName = "yduqs"
    elif companycode == 522:companyName = "yellowrec"
    elif companycode == 523:companyName = "youthvoices"
    elif companycode == 524:companyName = "zaffarinet"
    elif companycode == 525:companyName = "zallpy"
    elif companycode == 526:companyName = "zee-dog"
    elif companycode == 527:companyName = "zenvia"
    elif companycode == 528:companyName = "zoom-buscape"
    else:
        print ("companycode non ecziste!")

    url = 'https://'+companyName+'.gupy.io/'

    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    # find a list of all span elements
    spans = soup.find_all('span', {'class' : 'title'})

    # create a list of lines corresponding to element texts
    lines = [span.get_text() for span in spans]

    #coletando job link
    data = soup.findAll('a',attrs={'class':'job-list__item'})
    #coletando job description
    spans = soup.findAll('span', {'class' : 'title'})

    #coletando e tratando a localizacao
    dataLocal = soup.findAll('tr')#,attrs={'data-workplace':'Caxias do Sul'})

    my_listLocal = []
    for t in dataLocal:
        linkos = t.findAll('td')
        counti = 1
        for x in linkos:
            linkas = x.findAll('strong')
            #print(linkas)
            linkasF = str(linkas).replace("<strong>","").replace("</strong>","").replace("[]","")#.replace("]","").replace("[","")

            linkasF = ' '.join(linkasF.split())

            if linkasF == '[ ]':
                linkasF = "Verificar"

            linkasG = linkasF.replace("]","").replace("[","")
            
            #print(linkasG[0:30])

            #indexando as localizacao
            my_listLocal.append(linkasG)

            counti = counti + 1

#finalmente vou passar para a lista
    my_listLocalB = []
    countii = 0
    while countii < len(my_listLocal):
    
        if len(my_listLocal[countii]) < 1:
            ok = 1
        else:
            my_listLocalB.append(my_listLocal[countii])
            #print(my_listLocal[countii] + " " +str(countii))

        countii = countii + 1

    contaNo = 0
    while contaNo < len(my_listLocalB):
        #print("Looooop do my_listLocalB")
        #print(my_listLocalB[contaNo])
        contaNo = contaNo + 1

#indexando as URLS
    my_listURL = []
    for a in data:
        links = a.findAll('href')
        my_listURL.append(a['href'])
        #print(a['href'])


#indexando os titulos das vagas
    my_listTituloVaga = []
    for a in spans:
        links = a.findAll('title')
        my_listTituloVaga.append(a.text)

#para verificar se tem os cadastros
    #print('***********Tamanho das listas***********')
    #print("Lista de Titutos de Vagas: " + str(len(my_listTituloVaga)))
    #print("Lista de URLs: " + str(len(my_listURL)))
    #print("Lista de Localizacoes: " + str(len(my_listLocalB)))

#indexando todas as listas de cima
    a_dict = {}
    keyList = ["title", "url", "localizacao"]
    for i in keyList: 
        a_dict[i] = None

    finalList = []
    conta = 0
    while conta < len(my_listURL):
        #finalList.append(my_listTituloVaga[conta]+';'+url+my_listA[conta])
        
        a_dict = {'companyName': companyName,'title': my_listTituloVaga[conta],'url': url+my_listURL[conta], 'localizacao': my_listLocalB[conta]}
        finalList.append(dict(a_dict))
        #print(a_dict)
        conta += 1
    
    return finalList

contador = 1
while contador < 7:
    your_list_as_json = json.dumps(consultaVagas(contador),indent=1, sort_keys=True, ensure_ascii=False) 
    print(your_list_as_json)
    contador = contador + 1

y = json.loads(your_list_as_json)

#print(y)