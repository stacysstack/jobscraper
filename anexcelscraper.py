

#import requests
from bs4 import BeautifulSoup as Soup 
import urllib, requests, re, pandas as pd 
from collections import Counter



            characternumber = len(descript)

            wordnumber = len(descript.split())
            # print descript
            # sponsored = result.find({'sponsored'}).getText()
            # print sponsored
            # expired = result.find({'expired'}).getText()
            # print expired
            # uniqueID = company[0:1]+location[0:1]+date[5:7]+joburl[37:40]
            # print uniqueID     
            
            mascratio = masctotal/float(wordnumber)
            femratio = femtotal/float(wordnumber)

            df = df.append({
                
                #GEN INFO
                # 'A10-Unique ID': uniqueID, 
                'A11-Job Key': jobkey,
                'A12-Category': category,
                'A2-Job Title': jobtitle,
                'A30-Company': company, 
#                'A31-Country': country,
                'A32-State': state,
                'A33-City': city, 
#                'A34-Latitude': latitude,
#                'A35-Longitude': longitude,
                'A4-Location': location,
                'A7-Snippet': snippet, 
                'A8-Date': date, 
                'A9-Url': joburl, 
                'A91-Sponsored': sponsored, 
                'A92-Expired': expired, 
                'A921-Word Number': wordnumber,
                'A922-Characters':characternumber,
                'A93-Full description': descript,
                'A94-Masc Total': masctotal,
                'A96-Masc Ratio': mascratio,
                'A95-Fem Total': femtotal,
                'A97-Fem Ratio': femratio,
                #extras
                'A98-Male Extras': mascextras,
                'A99-Fem Extras': femextras,
                           
                # MASCULINE LIST
                'B1-Active': active, 
                'B2-Adventurous': advent, 
                'B3-Aggress': aggr,
                'B4-Ambitio': amb,
                'B5-Analy': anal,
                'B6-Assert': asser,
                'B7-Athlet': athl,
                'B8-Autonom': auto,
                'B9-Boast': boast,
                'C1-Challeng': chall,
                'C2-Compet': compet,
                'C3-Confi': conf,
                'C4-Cour': cour,
                'C5-Decide': decide,
                'C6-Decisive': decisive,
                'C7-Decision': decision,
                'C8-Determin': determin,
                'C9-Dominant': domin,
                'D1-Force': force,
                'D2-Greedy': greedy,
                'D3-Headstrong': headstrong,
                'D4-Hierarch': hierarchy,
                'D5-Hostil': hostil,
                'D6-Impulsive': impulsive,
                'D7-Independ': independen,
                'D8-Individual': individual,
                'D9-Intellect': intellect,
                'E1-Lead': lead,
                'E2-Logic': logic,
                'E3-Masculine': masculine,
                'E4-Objective': objective,
                'E5-Opinions': opinion,
                'E6-Outspoken': outspoken,
                'E7-Persist': persist,
                'E8-Principle': principle,
                'E9-Reckless': reckless, 
                'F1-Stubborn': stubborn,
                'F2-Superior': superior,
                'F3-Self-Confiden': selfconfid,
                'F4-Self-Suff': selfsufficien,
                'F5-Self-Relian': selfrelian,

                #mas extras
                'F6-Ninja': ninja,
                'F7-He': he,
                'F8-His': his,

                #FEMININE LIST
                'G1-Affect': affectionate,
                'G1-Child': child,
                'G2-Cheer': cheer,
                'G3-Commit': commit,
                'G4-Communal': communal,
                'G5-Compassion': compassion,
                'G6-Connect': connect,
                'G7-Considerate': considerate,
                'G8-Cooperat': cooperate,
                'G9-Depend': depend,
                'H1-Emotiona': emotiona,
                'H2-Empath': empath,
                'H3-Feminine': feminine,
                'H4-Flatterable': flatterable,
                'H5-Gentle': gentle,
                'H6-Honest': honest,
                'H7-Interpersonal': interpersonal,
                'H8-Interdependen': interdependen,
                'H9-Interpersona': interpersona,
                'I1-Kind': kind,
                'I2-Kinship': kinship,
                'I3-Loyal': loyal,
                'I4-Modesty': modesty,
                'I5-Nag': nag,
                'I6-Nurtur': nurtur,
                'I7-Pleasant': pleasant,
                'I8-Polite': polite,
                'I9-Quiet': quiet,
                'J1-Respon': respon,
                'J2-Sensitiv': sensitiv,
                'J3-Submissive': submissive,
                'J4-Support': support,
                'J5-Sympath': sympath,
                'J6-Tender': tender,
                'J7-Together': together,
                'J8-Trust': trust,
                'J9-Understand': understand,
                'K1-Warm': warm,
                'K2-Whin': whin,
                'K3-Yield': yiel,

                #femextras
                'K4-She': she, 
                'K5-Her': her,
                'K7-Hers': hers,

                #TEXTIO WORDS
                # 'K5-Inclusive': inclusive,
                # 'K6-Collaborat': collaborat,
                # 'K7-Contribut': contribute,
                # 'K8-Diplomacy': diplomacy,
                # 'K9-Passion': passion,
                # 'L0-Creat': creat,
                # 'L1-Wed Like': wedlike,
                # 'L2-Success Start': successstart,
                # 'L3-TellaStory': tellastory,
                # 'L4-Foster': foster,
                # 'L5-Progressive': progressive,
                # 'L6-Balancing': balancing,
                # 'L7-Family': family,
                # 'L8-Transparent': transparent,
                # 'L9-Strong Relation': strongrel,
                # 'M0-Comfortable': comfort,
                # 'M1-Team': team,
                # 'M2-Encourag': encourage,
                # 'M3-Embrace': embrace,
                # 'M4-Beautiful': beautiful,
                # 'M5-Care': care,
                # 'M6-Partner': partner,
                # 'M7-WithOthers': withothers,
                # 'M8-PartOf': partof,
                # 'M9-Imagine': imagine,
                # 'N0-Teach': teach,
                # 'N1-Strive': strive,
                # 'N2-Nourish': nourish,
                # 'N3-Come Join': comejoin,
                # 'N4-Openness': openness,
                # 'N5-Welcome': welcome,
                # 'N6-Meaning': meaning,


                }, 
                ignore_index=True)
    
        except IndexError:
 #            output_string = "/Users/stacy/Desktop/scraper/Data/"+inputdate+jobfield+".csv"
 #            df.to_csv(output_string, encoding="utf-8")

            # write new file
             output_string = "/Users/stacy/Desktop/scraper/Summer2017Data/summerdata"+jobfield+".csv"
             df.to_csv(output_string, encoding="utf-8")

            # append existing file 
            #  output_string = "/Users/stacy/Desktop/scraper/Data/fulldata.csv"
            #  df.to_csv(output_string, mode = 'a', header = False, encoding="utf-8")
             
             raise

df

# output_string = "/Users/stacy/Desktop/scraper/Data/"+inputdate+jobfield+".csv"
# output_string = "/Users/stacy/Desktop/scraper/Data/fulldata.csv"

#append existing file
# output_string = "/Users/stacy/Desktop/scraper/Data/fulldata"+jobfield+".csv"
# df.to_csv(output_string, mode = 'a', header = False, encoding="utf-8")

#write new file
output_string = "/Users/stacy/Desktop/scraper/Summer2017Data/summerdata"+jobfield+".csv"
df.to_csv(output_string, encoding="utf-8")
