import sys
from make_batch import build_batch

# Batch 3: The Golden Girls & Designing Women (Iconic Ensembles & Sharp Wit)
# 100 questions: 30 d1, 40 d2, 30 d3

questions = [
    # The Golden Girls - Textual / Plot / Characters
    (
        "Who played the sarcastic substitute teacher Dorothy Zbornak on The Golden Girls?",
        "Bea Arthur",
        ["Betty White", "Rue McClanahan", "Estelle Getty"],
        1
    ),
    (
        "Which actress played the sweet, naive Minnesotan Rose Nylund on The Golden Girls?",
        "Betty White",
        ["Bea Arthur", "Rue McClanahan", "Estelle Getty"],
        1
    ),
    (
        "Which actress played the flirtatious southern belle Blanche Devereaux on The Golden Girls?",
        "Rue McClanahan",
        ["Dixie Carter", "Delta Burke", "Betty White"],
        1
    ),
    (
        "Who played Dorothy's feisty, wisecracking Sicilian mother Sophia Petrillo on The Golden Girls?",
        "Estelle Getty",
        ["Bea Arthur", "Rue McClanahan", "Alice Ghostley"],
        1
    ),
    (
        "What was the fictional Minnesota hometown that Rose Nylund constantly told bizarre stories about?",
        "St. Olaf",
        ["Lake Wobegon", "Brainerd", "Little Falls"],
        1
    ),
    (
        "What catchphrase did Sophia Petrillo use to begin almost all of her autobiographical anecdotes?",
        "Picture it: Sicily, 1922...",
        ["Listen up, girls...", "Back in the old country...", "When I was in Palermo..."],
        1
    ),
    (
        "What was the name of the nursing home that Sophia Petrillo lived in before it burned down in the pilot?",
        "Shady Pines",
        ["Sunny Acres", "Whispering Palms", "Biscayne Bay Manor"],
        1
    ),
    (
        "What two-word threat did Dorothy frequently make whenever Sophia acted out of line?",
        "Shady Pines, Ma!",
        ["Back to Sicily!", "No more cannoli!", "To your room!"],
        1
    ),
    (
        "What late-night dessert did the four women constantly gather around the kitchen table to eat while discussing their problems?",
        "Cheesecake",
        ["Cannoli", "Key lime pie", "Ice cream sundaes"],
        1
    ),
    (
        "What street address in Miami did the women share on The Golden Girls?",
        "6151 Richmond Street",
        ["432 Ocean Drive", "742 Evergreen Terrace", "1049 Biscayne Boulevard"],
        2
    ),
    (
        "Who was the legal owner of the Miami home where the four women lived?",
        "Blanche Devereaux",
        ["Dorothy Zbornak", "Rose Nylund", "Sophia Petrillo"],
        1
    ),
    (
        "What was the name of Dorothy's cheating ex-husband, played by Herb Edelman, who wore a toupee?",
        "Stan Zbornak",
        ["George Devereaux", "Charlie Nylund", "Miles Webber"],
        1
    ),
    (
        "What novelty item did Dorothy's ex-husband Stan invent and try to market in season 5?",
        "The Zbornee open-and-shut potato peeler",
        ["The singing fish plaque", "The pet rock leash", "The solar-powered flashlight"],
        3
    ),
    (
        "What was the name of Rose Nylund's deceased husband whom she frequently reminisced about?",
        "Charlie Nylund",
        ["Miles Webber", "Sal Petrillo", "Stan Zbornak"],
        1
    ),
    (
        "What was the name of the college professor who became Rose Nylund's long-term boyfriend?",
        "Miles Webber",
        ["Hal Linden", "Buzz Belmont", "Arnie Peterson"],
        1
    ),
    (
        "Which veteran actor portrayed Rose's boyfriend Miles Webber, who was later revealed to be in Witness Protection?",
        "Harold Gould",
        ["Herb Edelman", "Leslie Nielsen", "Don Ameche"],
        2
    ),
    (
        "In the season 6 storyline, what was Miles Webber's real identity in the federal Witness Protection Program?",
        "Nicholas Carbone",
        ["Salvatore Rossi", "Vincenzo DeLuca", "Dominic Santini"],
        3
    ),
    (
        "What was the name of Blanche's beloved deceased husband?",
        "George Devereaux",
        ["Big Daddy Hollingsworth", "Lucas Hollingsworth", "Clayton Devereaux"],
        2
    ),
    (
        "What was Blanche Devereaux's father affectionately known as?",
        "Big Daddy",
        ["Colonel Curtis", "Papa Bear", "Judge Hollingsworth"],
        1
    ),
    (
        "Which actor played Blanche's wealthy southern father 'Big Daddy' Hollingsworth in his first appearances?",
        "Murray Hamilton",
        ["David Huddleston", "Denver Pyle", "Hoyt Axton"],
        3
    ),
    (
        "Which actor took over the role of Big Daddy in later episodes of The Golden Girls?",
        "David Huddleston",
        ["Murray Hamilton", "Pat Hingle", "Charles Durning"],
        3
    ),
    (
        "What was the name of Blanche's gay brother who visited and came out in the season 4 episode 'Scandal'?",
        "Clayton",
        ["Charmaine", "Virginia", "Skippy"],
        2
    ),
    (
        "Which actor played Blanche's brother Clayton Devereaux?",
        "Monte Markham",
        ["Richard Mulligan", "Peter Graves", "George Clooney"],
        3
    ),
    (
        "What was the name of Sophia Petrillo's deceased husband and Dorothy's father?",
        "Salvatore Petrillo",
        ["Guido Petrillo", "Antonio Petrillo", "Mario Petrillo"],
        2
    ),
    (
        "What famous accessory did Sophia Petrillo carry with her everywhere, even inside her own house?",
        "A wicker/straw handbag",
        ["A wooden rosary", "A red parasol", "A leather coin purse"],
        1
    ),
    (
        "What was Dorothy Zbornak's maiden name?",
        "Petrillo",
        ["Hollingsworth", "Lindstrom", "Gisborne"],
        1
    ),
    (
        "In the pilot episode of The Golden Girls, what gay cook lived with the women before being dropped from the series?",
        "Coco",
        ["Pepe", "Mateo", "Marco"],
        2
    ),
    (
        "Which actor played the housekeeper/cook Coco in the pilot of The Golden Girls?",
        "Charles Levin",
        ["Meshach Taylor", "Hector Elizondo", "Bronson Pinchot"],
        3
    ),
    (
        "Who created and wrote the pilot for The Golden Girls?",
        "Susan Harris",
        ["Linda Bloodworth-Thomason", "Diane English", "Marta Kauffman"],
        2
    ),
    (
        "Which production company created The Golden Girls along with Soap and Empty Nest?",
        "Witt/Thomas/Harris Productions",
        ["Miller-Boyett Productions", "Tandem Productions", "MTM Enterprises"],
        2
    ),
    (
        "Who wrote and originally recorded the theme song 'Thank You for Being a Friend' in 1978?",
        "Andrew Gold",
        ["Paul Williams", "Cynthia Fee", "Burt Bacharach"],
        2
    ),
    (
        "Which vocalist recorded the version of 'Thank You for Being a Friend' used as The Golden Girls theme?",
        "Cynthia Fee",
        ["Rita Coolidge", "Juice Newton", "Jennifer Warnes"],
        3
    ),
    (
        "Which roles were Betty White and Rue McClanahan originally offered before director Jay Sandrich suggested they swap?",
        "Betty White was offered Blanche, and Rue McClanahan was offered Rose",
        ["Betty White was offered Dorothy, and Rue McClanahan was offered Blanche", "Rue McClanahan was offered Sophia, and Betty White was offered Dorothy", "Betty White was offered Dorothy, and Rue McClanahan was offered Rose"],
        3
    ),
    (
        "Why did director Jay Sandrich suggest that Betty White and Rue McClanahan switch roles?",
        "To prevent them from typecasting roles similar to Sue Ann Nivens and Vivian Cavender",
        ["Because Bea Arthur refused to work with Betty as Blanche", "Because network executives felt Rue was too wholesome for Blanche", "Due to wardrobe fit issues during camera tests"],
        2
    ),
    (
        "What surprising age relationship existed between Estelle Getty and Bea Arthur in real life?",
        "Estelle Getty was roughly one year younger than Bea Arthur",
        ["Estelle Getty was 20 years older than Bea Arthur", "Estelle Getty and Bea Arthur were twin sisters", "Estelle Getty was 15 years younger than Bea Arthur"],
        3
    ),
    (
        "What rare Emmy distinction does The Golden Girls share with All in the Family and Will & Grace?",
        "All four principal cast members won Primetime Emmy Awards for their roles",
        ["It won Best Comedy Series for five consecutive years", "Every episode was nominated for an Emmy", "It swept all writing and directing categories in a single year"],
        2
    ),
    (
        "In which years did The Golden Girls win the Primetime Emmy Award for Outstanding Comedy Series?",
        "1986 and 1987",
        ["1985 and 1986", "1987 and 1988", "1988 and 1989"],
        3
    ),
    (
        "Which Golden Girl won the Primetime Emmy Award for Outstanding Lead Actress in a Comedy Series first, in 1986?",
        "Betty White",
        ["Bea Arthur", "Rue McClanahan", "Estelle Getty"],
        2
    ),
    (
        "What real-life culinary quirk did Bea Arthur have regarding the cheesecakes featured so prominently on the show?",
        "She actually hated cheesecake in real life",
        ["She was severely lactose intolerant", "She insisted on baking every cheesecake herself", "She only ate vegan cheesecake"],
        2
    ),
    (
        "What was the name of the 1992 spin-off series in which Rose, Blanche, and Sophia bought and ran a hotel?",
        "The Golden Palace",
        ["Golden Years", "Miami Palms Hotel", "The Richmond Inn"],
        1
    ),
    (
        "Which acclaimed actor played the hotel manager Chuy Castillos in the spin-off The Golden Palace?",
        "Cheech Marin",
        ["Paul Rodriguez", "Jimmy Smits", "Edward James Olmos"],
        2
    ),
    (
        "Which young future superstar played the hotel's foster child Oliver Webb on The Golden Palace?",
        "Billy L. Sullivan",
        ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elijah Wood"],
        3
    ),
    (
        "Who did Dorothy Zbornak marry in the series finale of The Golden Girls?",
        "Lucas Hollingsworth (Blanche's uncle)",
        ["Stan Zbornak", "Miles Webber", "Dr. Harry Weston"],
        2
    ),
    (
        "Which comedy legend played Blanche's uncle Lucas Hollingsworth, whom Dorothy married in the finale?",
        "Leslie Nielsen",
        ["Bob Newhart", "Gene Wilder", "Dick Van Dyke"],
        1
    ),
    (
        "What neighbor doctor starred in the spin-off Empty Nest, which was introduced via The Golden Girls?",
        "Dr. Harry Weston",
        ["Dr. Mark Craig", "Dr. Donald Westphall", "Dr. Wayne Fiscus"],
        2
    ),
    (
        "Which actor played pediatrician Dr. Harry Weston on Empty Nest and The Golden Girls?",
        "Richard Mulligan",
        ["Harold Gould", "Ed Begley Jr.", "Herb Edelman"],
        2
    ),
    (
        "What was the name of Dr. Harry Weston's large, lovable dog on Empty Nest?",
        "Dreyfuss",
        ["Barnaby", "Hercules", "Zeus"],
        2
    ),
    (
        "In the season 2 episode 'Isn't It Romantic?', who visited Dorothy and fell in love with Rose?",
        "Dorothy's lesbian friend Jean",
        ["Dorothy's high school art teacher", "Blanche's former sorority sister", "Sophia's cousin from Palermo"],
        2
    ),
    (
        "Which actress played Dorothy's friend Jean in 'Isn't It Romantic?'",
        "Lois Nettleton",
        ["Lee Grant", "Piper Laurie", "Shirley Jones"],
        3
    ),
    (
        "What musical guest star played a teenage boy named Mario who was tutored by Dorothy before facing deportation?",
        "Mario Lopez",
        ["Ricky Martin", "Mark-Paul Gosselaar", "Brian Austin Green"],
        2
    ),

    # Designing Women - Textual / Plot / Characters
    (
        "What was the name of the Atlanta interior design firm in Designing Women?",
        "Sugarbaker & Associates",
        ["Atlanta Fine Interiors", "Southern Elegance Designs", "Peachtree Decorators"],
        1
    ),
    (
        "Which actress played the eloquent, fiery feminist Julia Sugarbaker on Designing Women?",
        "Dixie Carter",
        ["Delta Burke", "Annie Potts", "Jean Smart"],
        1
    ),
    (
        "What intimidating nickname was Julia Sugarbaker known by due to her blistering takedowns?",
        "The Terminator",
        ["The Iron Magnolia", "The Hammer", "The Velvet Steamroller"],
        1
    ),
    (
        "What famous beauty title had Suzanne Sugarbaker won in 1975 on Designing Women?",
        "Miss Georgia",
        ["Miss America", "Miss Atlanta", "Miss Deep South"],
        1
    ),
    (
        "Which actress starred as the self-centered, beauty-obsessed Suzanne Sugarbaker?",
        "Delta Burke",
        ["Dixie Carter", "Annie Potts", "Jean Smart"],
        1
    ),
    (
        "What unusual pet did Suzanne Sugarbaker adopt and pamper in season 1 of Designing Women?",
        "A pet pig named Noelle",
        ["A white poodle named Bijou", "A cockatoo named Rhett", "A ferret named Bandit"],
        2
    ),
    (
        "Which actress played the pragmatic, divorced head designer Mary Jo Shively on Designing Women?",
        "Annie Potts",
        ["Dixie Carter", "Delta Burke", "Jean Smart"],
        1
    ),
    (
        "Which actress played the sweet-natured, naive office manager Charlene Frazier on Designing Women?",
        "Jean Smart",
        ["Annie Potts", "Dixie Carter", "Delta Burke"],
        1
    ),
    (
        "Which country music icon was Charlene Frazier completely obsessed with throughout Designing Women?",
        "Dolly Parton",
        ["Reba McEntire", "Loretta Lynn", "Tammy Wynette"],
        1
    ),
    (
        "What Missouri town did Charlene Frazier proudly hail from on Designing Women?",
        "Poplar Bluff",
        ["Cape Girardeau", "Branson", "Joplin"],
        2
    ),
    (
        "Who played Anthony Bouvier, the reformed ex-con who became deliveryman and partner at Sugarbaker's?",
        "Meshach Taylor",
        ["Carl Weathers", "Robert Guillaume", "Taurean Blacque"],
        1
    ),
    (
        "For what crime had Anthony Bouvier been falsely imprisoned before joining Sugarbaker & Associates?",
        "Aggravated robbery of a grocery store",
        ["Embezzlement from an auto dealership", "Grand theft auto", "Securities fraud"],
        3
    ),
    (
        "Who created and was the primary writer for Designing Women?",
        "Linda Bloodworth-Thomason",
        ["Susan Harris", "Diane English", "Marta Kauffman"],
        2
    ),
    (
        "Which director and producer, husband of Linda Bloodworth-Thomason, co-produced Designing Women?",
        "Harry Thomason",
        ["Paul Junger Witt", "Tony Thomas", "James Burrows"],
        2
    ),
    (
        "What arrangement did Dixie Carter make with the creators whenever Julia delivered a liberal monologue?",
        "Dixie was permitted to sing a musical number in a subsequent episode",
        ["She received additional executive producer credit", "The show donated money to her chosen charity", "Her real-life husband was given a guest starring role"],
        3
    ),
    (
        "What famous monologue did Julia Sugarbaker deliver in defense of Suzanne to a snobbish pageant winner?",
        "The 'And that, Marjorie, is how the lights went out in Georgia' speech",
        ["The 'Southern Belles Do Not Bow' speech", "The 'Magnolias with Steel Spines' address", "The 'Crowns Don't Tarnish' tirade"],
        1
    ),
    (
        "Which actress played the eccentric, delightfully batty friend Bernice Clifton on Designing Women?",
        "Alice Ghostley",
        ["Estelle Getty", "Charlotte Rae", "Marion Ross"],
        2
    ),
    (
        "What real-life husband of Dixie Carter guest-starred as Suzanne's novelist ex-husband, Dash Goff?",
        "Gerald McRaney",
        ["Hal Holbrook", "Robert Foxworth", "Richard Mulligan"],
        2
    ),
    (
        "What was the name of Suzanne's novelist ex-husband played by Gerald McRaney?",
        "Dash Goff",
        ["Jack Dent", "Reggie Mac Dawson", "Sonny Crawford"],
        2
    ),
    (
        "Which actor played Julia Sugarbaker's long-term lawyer boyfriend Reese Watson?",
        "Hal Holbrook",
        ["Gerald McRaney", "Richard Mulligan", "Charles Durning"],
        2
    ),
    (
        "What was the relationship between Hal Holbrook and Dixie Carter in real life?",
        "They were married",
        ["They were brother and sister", "They were first cousins", "They were former college classmates"],
        2
    ),
    (
        "How was Reese Watson written out of Designing Women in season 5 following actor Hal Holbrook's departure?",
        "He suffered a sudden fatal heart attack off screen",
        ["He moved to Washington D.C. permanently", "He married another woman in Europe", "He died in a courtroom explosion"],
        3
    ),
    (
        "What broadcast network was the home of Designing Women throughout its original run?",
        "CBS",
        ["NBC", "ABC", "Fox"],
        1
    ),
    (
        "What night of the week became the signature home for Designing Women alongside Murphy Brown?",
        "Monday night",
        ["Thursday night", "Sunday night", "Wednesday night"],
        2
    ),
    (
        "In 1987, CBS nearly canceled Designing Women due to low ratings before what grassroots movement saved it?",
        "Viewers for Quality Television letter-writing campaign",
        ["A protest rally at Rockefeller Center", "A sponsor boycott organized by Ford", "A celebrity telethon hosted by Dolly Parton"],
        3
    ),
    (
        "Which character did Charlene Frazier marry in season 4 of Designing Women?",
        "Bill Stillfield",
        ["Dash Goff", "Ray Don Simpson", "Ted Shively"],
        2
    ),
    (
        "What branch of the U.S. military did Charlene's husband Bill Stillfield serve in?",
        "Air Force (Colonel)",
        ["Navy (Commander)", "Army (Captain)", "Marines (Major)"],
        3
    ),
    (
        "Which actor played Charlene's Air Force husband Bill Stillfield?",
        "Douglas Barr",
        ["Gerald McRaney", "Jameson Parker", "Lee Majors"],
        3
    ),
    (
        "Which guest star played Charlene's baby's guardian angel in the hospital during childbirth in season 4?",
        "Dolly Parton",
        ["Kenny Rogers", "Tammy Wynette", "Willie Nelson"],
        2
    ),
    (
        "What was the name of Charlene and Bill's baby daughter, born in season 4?",
        "Olivia",
        ["Noelle", "Savannah", "Georgia"],
        3
    ),
    (
        "What highly publicized conflict led to Delta Burke being fired from Designing Women after season 5?",
        "Bitter behind-the-scenes feuds with creator Linda Bloodworth-Thomason and producers",
        ["A contract holdout demanding equal pay to network executives", "Her refusal to film outside Atlanta", "An arrest for driving under the influence"],
        2
    ),
    (
        "Which two actresses were brought in to replace Delta Burke and Jean Smart in season 6 of Designing Women?",
        "Julia Duffy and Jan Hooks",
        ["Delta Burke and Dixie Carter", "Priscilla Presley and Annie Potts", "Morgan Fairchild and Loni Anderson"],
        2
    ),
    (
        "What character did Jan Hooks play starting in season 6 of Designing Women?",
        "Carlene Frazier Dobber (Charlene's sister)",
        ["Allison Sugarbaker", "BJ Poteet", "Rusty Vandermeer"],
        1
    ),
    (
        "What character did Julia Duffy play during season 6 before leaving the series?",
        "Allison Sugarbaker (Julia and Suzanne's snobbish cousin)",
        ["Carlene Dobber", "BJ Poteet", "Bernice Clifton"],
        3
    ),
    (
        "Which actress joined Designing Women in season 7 as wealthy widow B.J. Poteet?",
        "Judith Ivey",
        ["Julia Duffy", "Morgan Fairchild", "Rue McClanahan"],
        3
    ),
    (
        "What prestigious law degree did Anthony Bouvier work toward earning during the later seasons of Designing Women?",
        "Juris Doctor from night law school",
        ["Master of Business Administration", "Doctor of Architecture", "Certified Public Accountant"],
        2
    ),
    (
        "Which Designing Women episode famously addressed the AIDS crisis and stigma in 1987?",
        "Killing All the Right People",
        ["The Night the Lights Went Out", "One Flew Over the Sugarbaker's", "reservations for Eight"],
        2
    ),
    (
        "In 'Killing All the Right People', what young decorator asked Sugarbaker's to plan his funeral before dying of AIDS?",
        "Kendall Truman",
        ["Tony Henderson", "Mark Simpson", "David Ray"],
        3
    ),
    (
        "Which actor played Kendall Truman in the landmark episode 'Killing All the Right People'?",
        "Tony Goldwyn",
        ["Campbell Scott", "Dermot Mulroney", "Eric Stoltz"],
        3
    ),
    (
        "What instrument did Julia Sugarbaker play when performing 'The Night the Lights Went Out in Georgia'?",
        "Piano",
        ["Harp", "Violin", "Acoustic guitar"],
        2
    ),
    (
        "Which Southern governor and future U.S. President was close personal friends with creators Linda and Harry Thomason?",
        "Bill Clinton",
        ["Jimmy Carter", "George H.W. Bush", "Ronald Reagan"],
        2
    ),
    (
        "What documentary film did Harry Thomason and Linda Bloodworth-Thomason produce for Bill Clinton's 1992 campaign?",
        "The Man from Hope",
        ["A Place Called Hope", "Arkansas Traveler", "Journey to the White House"],
        3
    ),
    (
        "In season 2 of Designing Women, what beauty pageant did Suzanne enter Anthony in as a joke?",
        "The Miss General Motors Pageant (as a chaperone)",
        ["Mr. Atlanta Physique", "The Georgia Bachelor Contest", "Southern Gentleman of the Year"],
        3
    ),
    (
        "What was Mary Jo Shively's ex-husband's profession on Designing Women?",
        "Gynecologist / Obstetrician",
        ["Divorce attorney", "Commercial airline pilot", "Car salesman"],
        3
    ),
    (
        "Which actor played Ted Shively, Mary Jo's cheating ex-husband?",
        "Scott Bakula",
        ["Gerald McRaney", "Richard Gilliland", "Terry Kiser"],
        3
    ),
    (
        "Which actor, who played J.D. Shackelford (Mary Jo's boyfriend), was married to Jean Smart in real life?",
        "Richard Gilliland",
        ["Hal Holbrook", "Gerald McRaney", "Douglas Barr"],
        3
    ),
    (
        "How many seasons did Designing Women air on CBS from 1986 to 1993?",
        "7 seasons",
        ["5 seasons", "6 seasons", "8 seasons"],
        2
    ),
    (
        "What Georgia historic Victorian house was used for the exterior shots of the Sugarbaker design firm?",
        "The Villa Marre in Little Rock, Arkansas",
        ["Swan House in Atlanta", "Rhodes Hall in Midtown Atlanta", "The Mercer House in Savannah"],
        3
    ),
    (
        "Why was an Arkansas Victorian home used as the exterior for Designing Women instead of one in Atlanta?",
        "Producers Linda and Harry Thomason were Arkansas natives and loved the house",
        ["Atlanta city ordinances banned commercial filming of homes", "The Atlanta location burned down before filming", "It was cheaper to ship the film crew to Little Rock"],
        3
    ),
    (
        "Which spin-off series centered on Delta Burke's character Suzanne Sugarbaker moving to Washington D.C.?",
        "Women of the House",
        ["Suzanne in the Capital", "First Lady", "The Sugarbaker Legacy"],
        2
    )
]

if __name__ == "__main__":
    build_batch(questions, 3, "tools/staging/80s_tv_shows_batch3.json")
