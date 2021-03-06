// This script automates using google search to get mrt opening years
// As with most web automation, you will not get all results. Thus some manual work is require to get the empty results

// TO DO: generate array from raw data, instead of using a hardcoded array
const stations = [
  'ADMIRALTY MRT STATION','ALJUNIED MRT STATION', 'ANG MO KIO MRT STATION', 'BAKAU LRT STATION', 'BANGKIT LRT STATION', 'BARTLEY MRT STATION', 'BAYFRONT MRT STATION', 'BEAUTY WORLD MRT STATION',
  'BEDOK MRT STATION', 'BEDOK NORTH MRT STATION', 'BEDOK RESERVOIR MRT STATION', 'BENCOOLEN MRT STATION', 'BENDEMEER MRT STATION', 'BISHAN MRT STATION', 'BOON KENG MRT STATION', 'BOON LAY MRT STATION',
  'BOTANIC GARDENS MRT STATION', 'BRADDELL MRT STATION', 'BRAS BASAH MRT STATION', 'BUANGKOK MRT STATION', 'BUGIS MRT STATION', 'BUKIT BATOK MRT STATION', 'BUKIT BROWN MRT STATION', 'BUKIT GOMBAK MRT STATION',
  'BUKIT PANJANG LRT STATION', 'BUKIT PANJANG MRT STATION', 'BUONA VISTA MRT STATION', 'CALDECOTT MRT STATION', 'CANBERRA MRT STATION', 'CASHEW MRT STATION', 'CHANGI AIRPORT MRT STATION',
  'CHENG LIM LRT STATION', 'CHINATOWN MRT STATION', 'CHINESE GARDEN MRT STATION', 'CHOA CHU KANG LRT STATION', 'CHOA CHU KANG MRT STATION', 'CITY HALL MRT STATION', 'CLARKE QUAY MRT STATION',
  'CLEMENTI MRT STATION', 'COMMONWEALTH MRT STATION', 'COMPASSVALE LRT STATION', 'CORAL EDGE LRT STATION', 'COVE LRT STATION', 'DAKOTA MRT STATION', 'DAMAI LRT STATION', 'DHOBY GHAUT MRT STATION',
  'DOVER MRT STATION', 'DOWNTOWN MRT STATION', 'ESPLANADE MRT STATION', 'EUNOS MRT STATION', 'EXPO MRT STATION', 'FAJAR LRT STATION', 'FARMWAY LRT STATION', 'FARRER PARK MRT STATION', 'FARRER ROAD MRT STATION',
  'FERNVALE LRT STATION', 'FORT CANNING MRT STATION', 'GEYLANG BAHRU MRT STATION', 'GUL CIRCLE MRT STATION', 'HARBOURFRONT MRT STATION', 'HAW PAR VILLA MRT STATION', 'HILLVIEW MRT STATION', 'HOLLAND VILLAGE MRT STATION',
  'HOUGANG MRT STATION', 'JALAN BESAR MRT STATION', 'JELAPANG LRT STATION', 'JOO KOON MRT STATION', 'JURONG EAST MRT STATION', 'KADALOOR LRT STATION', 'KAKI BUKIT MRT STATION', 'KALLANG MRT STATION',
  'KANGKAR LRT STATION', 'KEAT HONG LRT STATION', 'KEMBANGAN MRT STATION', 'KENT RIDGE MRT STATION', 'KHATIB MRT STATION', 'KING ALBERT PARK MRT STATION', 'KOVAN MRT STATION', 'KRANJI MRT STATION',
  'KUPANG LRT STATION', 'LABRADOR PARK MRT STATION', 'LAKESIDE MRT STATION', 'LAVENDER MRT STATION', 'LAYAR LRT STATION', 'LITTLE INDIA MRT STATION', 'LORONG CHUAN MRT STATION',
  'MACPHERSON MRT STATION', 'MARINA BAY MRT STATION', 'MARINA SOUTH PIER MRT STATION', 'MARSILING MRT STATION', 'MARYMOUNT MRT STATION', 'MATTAR MRT STATION', 'MERIDIAN LRT STATION',
  'MOUNTBATTEN MRT STATION', 'NEWTON MRT STATION', 'NIBONG LRT STATION', 'NICOLL HIGHWAY MRT STATION', 'NOVENA MRT STATION', 'OASIS LRT STATION', 'ONE-NORTH MRT STATION', 'ORCHARD MRT STATION',
  'OUTRAM PARK MRT STATION', 'PASIR PANJANG MRT STATION', 'PASIR RIS MRT STATION', 'PAYA LEBAR MRT STATION', 'PENDING LRT STATION', 'PETIR LRT STATION', 'PHOENIX LRT STATION', 'PIONEER MRT STATION',
  'POTONG PASIR MRT STATION', 'PROMENADE MRT STATION', 'PUNGGOL LRT STATION', 'PUNGGOL MRT STATION', 'PUNGGOL POINT LRT STATION', 'QUEENSTOWN MRT STATION', 'RAFFLES PLACE MRT STATION', 'RANGGUNG LRT STATION',
  'REDHILL MRT STATION', 'RENJONG LRT STATION', 'RIVIERA LRT STATION', 'ROCHOR MRT STATION', 'RUMBIA LRT STATION', 'SAM KEE LRT STATION', 'SAMUDERA LRT STATION', 'SEGAR LRT STATION', 'SEMBAWANG MRT STATION',
  'SENGKANG LRT STATION', 'SENGKANG MRT STATION', 'SENJA LRT STATION', 'SERANGOON MRT STATION', 'SIMEI MRT STATION', 'SIXTH AVENUE MRT STATION', 'SOMERSET MRT STATION', 'SOO TECK LRT STATION', 'SOUTH VIEW LRT STATION',
  'STADIUM MRT STATION', 'STEVENS MRT STATION', 'SUMANG LRT STATION', 'TAI SENG MRT STATION', 'TAMPINES EAST MRT STATION', 'TAMPINES MRT STATION', 'TAMPINES WEST MRT STATION', 'TAN KAH KEE MRT STATION',
  'TANAH MERAH MRT STATION', 'TANJONG PAGAR MRT STATION', 'TECK LEE LRT STATION', 'TECK WHYE LRT STATION', 'TELOK AYER MRT STATION', 'TELOK BLANGAH MRT STATION', 'TEN MILE JUNCTION LRT STATION',
  'THANGGAM LRT STATION', 'TIONG BAHRU MRT STATION', 'TOA PAYOH MRT STATION', 'TONGKANG LRT STATION', 'TUAS CRESCENT MRT STATION', 'TUAS LINK MRT STATION', 'TUAS WEST ROAD MRT STATION',
  'UBI MRT STATION', 'UPPER CHANGI MRT STATION', 'WOODLANDS MRT STATION', 'WOODLANDS NORTH MRT STATION', 'WOODLANDS SOUTH MRT STATION', 'WOODLEIGH MRT STATION', 'YEW TEE MRT STATION',
  'YIO CHU KANG MRT STATION', 'YISHUN MRT STATION'
]

const fs = require('fs');
const puppeteer = require('puppeteer');

it.each(stations)('searching...', async (s) => {
  jest.setTimeout(60000);
  const browser = await puppeteer.launch(
    {
      headless: false,
      slowMo: 25,
      args: [`--window-size=${1200},${800}`] // new option
    }
  );
  const page = await browser.newPage();
  await page.goto('https://google.com');
  await page.type('input[name=q]', `${s} year of opening`, {delay: 20})
  const form = await page.$('input[name=btnK]');
  await form.evaluate( form => form.click() );
  await page.waitForTimeout(4000);

  try {
    const element = await page.$(".Z0LcW");
    const text = await page.evaluate(element => element.textContent, element);
    // console.log(text);
    fs.appendFileSync("mrt-opening-year-raw.csv", `${s}, ${text}\n`); 
  } catch (err) {
    console.log("Not found!");
  }

  await browser.close();
});
