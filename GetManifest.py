from bs4 import BeautifulSoup
import re

html = """<tr>
<td class="text-right">16 July 2022 – 13:44:48 UTC</td>
<td class="timeago" data-time="2022-07-16T13:44:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5466015679443468050" rel="nofollow">5466015679443468050</a>
</td>
</tr>
<tr>
<td class="text-right">15 July 2022 – 20:10:36 UTC</td>
<td class="timeago" data-time="2022-07-15T20:10:36+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6015002708928976081" rel="nofollow">6015002708928976081</a>
</td>
</tr>
<tr>
<td class="text-right">11 July 2022 – 14:40:11 UTC</td>
<td class="timeago" data-time="2022-07-11T14:40:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1981964167712894722" rel="nofollow">1981964167712894722</a>
</td>
</tr>
<tr>
<td class="text-right">25 June 2022 – 15:09:25 UTC</td>
<td class="timeago" data-time="2022-06-25T15:09:25+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7443885648242173844" rel="nofollow">7443885648242173844</a>
</td>
</tr>
<tr>
<td class="text-right">25 June 2022 – 14:04:46 UTC</td>
<td class="timeago" data-time="2022-06-25T14:04:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5054641598797083963" rel="nofollow">5054641598797083963</a>
</td>
</tr>
<tr>
<td class="text-right">15 June 2022 – 19:18:19 UTC</td>
<td class="timeago" data-time="2022-06-15T19:18:19+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3226898068550678108" rel="nofollow">3226898068550678108</a>
</td>
</tr>
<tr>
<td class="text-right">10 June 2022 – 15:00:10 UTC</td>
<td class="timeago" data-time="2022-06-10T15:00:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1461397219334598989" rel="nofollow">1461397219334598989</a>
</td>
</tr>
<tr>
<td class="text-right">28 April 2022 – 08:36:56 UTC</td>
<td class="timeago" data-time="2022-04-28T08:36:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5593150803555749056" rel="nofollow">5593150803555749056</a>
</td>
</tr>
<tr>
<td class="text-right">23 April 2022 – 11:46:44 UTC</td>
<td class="timeago" data-time="2022-04-23T11:46:44+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6656874366735233519" rel="nofollow">6656874366735233519</a>
</td>
</tr>
<tr>
<td class="text-right">21 April 2022 – 18:57:25 UTC</td>
<td class="timeago" data-time="2022-04-21T18:57:25+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6995685432931928229" rel="nofollow">6995685432931928229</a>
</td>
</tr>
<tr>
<td class="text-right">21 April 2022 – 18:36:19 UTC</td>
<td class="timeago" data-time="2022-04-21T18:36:19+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3249990818100181444" rel="nofollow">3249990818100181444</a>
</td>
</tr>
<tr>
<td class="text-right">21 April 2022 – 10:51:49 UTC</td>
<td class="timeago" data-time="2022-04-21T10:51:49+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8666937344672740211" rel="nofollow">8666937344672740211</a>
</td>
</tr>
<tr>
<td class="text-right">20 April 2022 – 09:43:23 UTC</td>
<td class="timeago" data-time="2022-04-20T09:43:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1833527785366495991" rel="nofollow">1833527785366495991</a>
</td>
</tr>
<tr>
<td class="text-right">16 April 2022 – 12:30:30 UTC</td>
<td class="timeago" data-time="2022-04-16T12:30:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8438965400719388894" rel="nofollow">8438965400719388894</a>
</td>
</tr>
<tr>
<td class="text-right">15 April 2022 – 10:36:02 UTC</td>
<td class="timeago" data-time="2022-04-15T10:36:02+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7455926422135730190" rel="nofollow">7455926422135730190</a>
</td>
</tr>
<tr>
<td class="text-right">13 April 2022 – 18:44:49 UTC</td>
<td class="timeago" data-time="2022-04-13T18:44:49+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9048803291175692844" rel="nofollow">9048803291175692844</a>
</td>
</tr>
<tr>
<td class="text-right">12 April 2022 – 15:33:02 UTC</td>
<td class="timeago" data-time="2022-04-12T15:33:02+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1148224753986084724" rel="nofollow">1148224753986084724</a>
</td>
</tr>
<tr>
<td class="text-right">12 April 2022 – 13:36:19 UTC</td>
<td class="timeago" data-time="2022-04-12T13:36:19+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1412670694714423903" rel="nofollow">1412670694714423903</a>
</td>
</tr>
<tr>
<td class="text-right">7 April 2022 – 19:49:08 UTC</td>
<td class="timeago" data-time="2022-04-07T19:49:08+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3340915552116401259" rel="nofollow">3340915552116401259</a>
</td>
</tr>
<tr>
<td class="text-right">7 April 2022 – 12:02:05 UTC</td>
<td class="timeago" data-time="2022-04-07T12:02:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8473400715065812048" rel="nofollow">8473400715065812048</a>
</td>
</tr>
<tr>
<td class="text-right">3 March 2022 – 21:17:51 UTC</td>
<td class="timeago" data-time="2022-03-03T21:17:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2925451301316479646" rel="nofollow">2925451301316479646</a>
</td>
</tr>
<tr>
<td class="text-right">10 February 2022 – 17:38:20 UTC</td>
<td class="timeago" data-time="2022-02-10T17:38:20+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3255613350159026121" rel="nofollow">3255613350159026121</a>
</td>
</tr>
<tr>
<td class="text-right">10 February 2022 – 16:58:11 UTC</td>
<td class="timeago" data-time="2022-02-10T16:58:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3688969080780143769" rel="nofollow">3688969080780143769</a>
</td>
</tr>
<tr>
<td class="text-right">20 January 2022 – 13:27:24 UTC</td>
<td class="timeago" data-time="2022-01-20T13:27:24+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3093250432330223724" rel="nofollow">3093250432330223724</a>
</td>
</tr>
<tr>
<td class="text-right">10 January 2022 – 11:44:55 UTC</td>
<td class="timeago" data-time="2022-01-10T11:44:55+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1539425284896419288" rel="nofollow">1539425284896419288</a>
</td>
</tr>
<tr>
<td class="text-right">24 December 2021 – 14:47:45 UTC</td>
<td class="timeago" data-time="2021-12-24T14:47:45+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7732646670689943302" rel="nofollow">7732646670689943302</a>
</td>
</tr>
<tr>
<td class="text-right">13 December 2021 – 22:30:10 UTC</td>
<td class="timeago" data-time="2021-12-13T22:30:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6050414862942411601" rel="nofollow">6050414862942411601</a>
</td>
</tr>
<tr>
<td class="text-right">10 December 2021 – 19:17:13 UTC</td>
<td class="timeago" data-time="2021-12-10T19:17:13+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5797001756337197113" rel="nofollow">5797001756337197113</a>
</td>
</tr>
<tr>
<td class="text-right">10 December 2021 – 16:01:20 UTC</td>
<td class="timeago" data-time="2021-12-10T16:01:20+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2616344252470314058" rel="nofollow">2616344252470314058</a>
</td>
</tr>
<tr>
<td class="text-right">12 November 2021 – 10:30:03 UTC</td>
<td class="timeago" data-time="2021-11-12T10:30:03+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1105060426474921575" rel="nofollow">1105060426474921575</a>
</td>
</tr>
<tr>
<td class="text-right">4 November 2021 – 17:27:00 UTC</td>
<td class="timeago" data-time="2021-11-04T17:27:00+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:520665518550656045" rel="nofollow">520665518550656045</a>
</td>
</tr>
<tr>
<td class="text-right">2 November 2021 – 22:11:54 UTC</td>
<td class="timeago" data-time="2021-11-02T22:11:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3685374349890939307" rel="nofollow">3685374349890939307</a>
</td>
</tr>
<tr>
<td class="text-right">2 November 2021 – 20:54:14 UTC</td>
<td class="timeago" data-time="2021-11-02T20:54:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4461829338815692774" rel="nofollow">4461829338815692774</a>
</td>
</tr>
<tr>
<td class="text-right">25 October 2021 – 23:23:06 UTC</td>
<td class="timeago" data-time="2021-10-25T23:23:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5119178702543197978" rel="nofollow">5119178702543197978</a>
</td>
</tr>
<tr>
<td class="text-right">25 October 2021 – 15:00:23 UTC</td>
<td class="timeago" data-time="2021-10-25T15:00:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2525466827460433101" rel="nofollow">2525466827460433101</a>
</td>
</tr>
<tr>
<td class="text-right">30 September 2021 – 17:45:59 UTC</td>
<td class="timeago" data-time="2021-09-30T17:45:59+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6237637267654798489" rel="nofollow">6237637267654798489</a>
</td>
</tr>
<tr>
<td class="text-right">29 September 2021 – 19:03:26 UTC</td>
<td class="timeago" data-time="2021-09-29T19:03:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3475225629057533835" rel="nofollow">3475225629057533835</a>
</td>
</tr>
<tr>
<td class="text-right">29 September 2021 – 17:41:01 UTC</td>
<td class="timeago" data-time="2021-09-29T17:41:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3275587103707275182" rel="nofollow">3275587103707275182</a>
</td>
</tr>
<tr>
<td class="text-right">21 September 2021 – 14:25:15 UTC</td>
<td class="timeago" data-time="2021-09-21T14:25:15+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3461631499780904807" rel="nofollow">3461631499780904807</a>
</td>
</tr>
<tr>
<td class="text-right">19 September 2021 – 10:32:35 UTC</td>
<td class="timeago" data-time="2021-09-19T10:32:35+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8977597945171945054" rel="nofollow">8977597945171945054</a>
</td>
</tr>
<tr>
<td class="text-right">18 September 2021 – 13:46:51 UTC</td>
<td class="timeago" data-time="2021-09-18T13:46:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8919724960624655543" rel="nofollow">8919724960624655543</a>
</td>
</tr>
<tr>
<td class="text-right">18 September 2021 – 10:17:54 UTC</td>
<td class="timeago" data-time="2021-09-18T10:17:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8642444708090526718" rel="nofollow">8642444708090526718</a>
</td>
</tr>
<tr>
<td class="text-right">8 September 2021 – 12:19:17 UTC</td>
<td class="timeago" data-time="2021-09-08T12:19:17+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4137531230169991024" rel="nofollow">4137531230169991024</a>
</td>
</tr>
<tr>
<td class="text-right">7 September 2021 – 13:27:23 UTC</td>
<td class="timeago" data-time="2021-09-07T13:27:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:821127493522811339" rel="nofollow">821127493522811339</a>
</td>
</tr>
<tr>
<td class="text-right">4 September 2021 – 00:55:26 UTC</td>
<td class="timeago" data-time="2021-09-04T00:55:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2395063308056314883" rel="nofollow">2395063308056314883</a>
</td>
</tr>
<tr>
<td class="text-right">3 September 2021 – 17:33:14 UTC</td>
<td class="timeago" data-time="2021-09-03T17:33:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5833307953638198140" rel="nofollow">5833307953638198140</a>
</td>
</tr>
<tr>
<td class="text-right">29 August 2021 – 13:26:28 UTC</td>
<td class="timeago" data-time="2021-08-29T13:26:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8710926232445935032" rel="nofollow">8710926232445935032</a>
</td>
</tr>
<tr>
<td class="text-right">27 August 2021 – 21:36:28 UTC</td>
<td class="timeago" data-time="2021-08-27T21:36:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2924494338731855928" rel="nofollow">2924494338731855928</a>
</td>
</tr>
<tr>
<td class="text-right">27 August 2021 – 18:03:06 UTC</td>
<td class="timeago" data-time="2021-08-27T18:03:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7042527042788907080" rel="nofollow">7042527042788907080</a>
</td>
</tr>
<tr>
<td class="text-right">26 August 2021 – 20:50:22 UTC</td>
<td class="timeago" data-time="2021-08-26T20:50:22+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5901281724570810674" rel="nofollow">5901281724570810674</a>
</td>
</tr>
<tr>
<td class="text-right">26 August 2021 – 18:00:12 UTC</td>
<td class="timeago" data-time="2021-08-26T18:00:12+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7225216050170498046" rel="nofollow">7225216050170498046</a>
</td>
</tr>
<tr>
<td class="text-right">21 July 2021 – 12:54:30 UTC</td>
<td class="timeago" data-time="2021-07-21T12:54:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6092585561508991135" rel="nofollow">6092585561508991135</a>
</td>
</tr>
<tr>
<td class="text-right">8 July 2021 – 14:16:27 UTC</td>
<td class="timeago" data-time="2021-07-08T14:16:27+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8504395138198409364" rel="nofollow">8504395138198409364</a>
</td>
</tr>
<tr>
<td class="text-right">8 July 2021 – 13:46:05 UTC</td>
<td class="timeago" data-time="2021-07-08T13:46:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4743248881756177777" rel="nofollow">4743248881756177777</a>
</td>
</tr>
<tr>
<td class="text-right">8 July 2021 – 10:39:46 UTC</td>
<td class="timeago" data-time="2021-07-08T10:39:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6198686189167166033" rel="nofollow">6198686189167166033</a>
</td>
</tr>
<tr>
<td class="text-right">4 July 2021 – 03:04:06 UTC</td>
<td class="timeago" data-time="2021-07-04T03:04:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1302687136711957942" rel="nofollow">1302687136711957942</a>
</td>
</tr>
<tr>
<td class="text-right">4 July 2021 – 02:05:16 UTC</td>
<td class="timeago" data-time="2021-07-04T02:05:16+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6764435358498433854" rel="nofollow">6764435358498433854</a>
</td>
</tr>
<tr>
<td class="text-right">3 July 2021 – 13:16:23 UTC</td>
<td class="timeago" data-time="2021-07-03T13:16:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2936572860801515350" rel="nofollow">2936572860801515350</a>
</td>
</tr>
<tr>
<td class="text-right">3 July 2021 – 01:43:00 UTC</td>
<td class="timeago" data-time="2021-07-03T01:43:00+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5969653076528981295" rel="nofollow">5969653076528981295</a>
</td>
</tr>
<tr>
<td class="text-right">24 June 2021 – 14:45:25 UTC</td>
<td class="timeago" data-time="2021-06-24T14:45:25+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:315427064834681429" rel="nofollow">315427064834681429</a>
</td>
</tr>
<tr>
<td class="text-right">23 June 2021 – 15:34:19 UTC</td>
<td class="timeago" data-time="2021-06-23T15:34:19+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2940737461481499678" rel="nofollow">2940737461481499678</a>
</td>
</tr>
<tr>
<td class="text-right">19 June 2021 – 19:15:11 UTC</td>
<td class="timeago" data-time="2021-06-19T19:15:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1941284572112489901" rel="nofollow">1941284572112489901</a>
</td>
</tr>
<tr>
<td class="text-right">17 June 2021 – 16:58:36 UTC</td>
<td class="timeago" data-time="2021-06-17T16:58:36+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4784675368519557028" rel="nofollow">4784675368519557028</a>
</td>
</tr>
<tr>
<td class="text-right">16 June 2021 – 21:45:09 UTC</td>
<td class="timeago" data-time="2021-06-16T21:45:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:923912611429040382" rel="nofollow">923912611429040382</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">15 June 2021 – 17:53:39 UTC</td>
<td class="timeago" data-time="2021-06-15T17:53:39+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3106186174201217035" rel="nofollow">3106186174201217035</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">15 June 2021 – 01:48:52 UTC</td>
<td class="timeago" data-time="2021-06-15T01:48:52+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2483464014469526013" rel="nofollow">2483464014469526013</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">14 June 2021 – 18:55:18 UTC</td>
<td class="timeago" data-time="2021-06-14T18:55:18+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2779540152861400621" rel="nofollow">2779540152861400621</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 June 2021 – 22:58:30 UTC</td>
<td class="timeago" data-time="2021-06-12T22:58:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2010553131874053401" rel="nofollow">2010553131874053401</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 June 2021 – 22:55:36 UTC</td>
<td class="timeago" data-time="2021-06-11T22:55:36+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3052127287323021405" rel="nofollow">3052127287323021405</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 June 2021 – 19:49:53 UTC</td>
<td class="timeago" data-time="2021-06-11T19:49:53+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5283579410178838717" rel="nofollow">5283579410178838717</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 June 2021 – 17:01:54 UTC</td>
<td class="timeago" data-time="2021-06-11T17:01:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3670251924775371407" rel="nofollow">3670251924775371407</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">14 May 2021 – 19:28:51 UTC</td>
<td class="timeago" data-time="2021-05-14T19:28:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7218018814119065181" rel="nofollow">7218018814119065181</a>
</td>
</tr>
<tr>
<td class="text-right">7 May 2021 – 18:47:41 UTC</td>
<td class="timeago" data-time="2021-05-07T18:47:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1975428935839111928" rel="nofollow">1975428935839111928</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">6 May 2021 – 16:40:38 UTC</td>
<td class="timeago" data-time="2021-05-06T16:40:38+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6233647281389273185" rel="nofollow">6233647281389273185</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">6 May 2021 – 15:40:06 UTC</td>
<td class="timeago" data-time="2021-05-06T15:40:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1637470070491878620" rel="nofollow">1637470070491878620</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">5 May 2021 – 16:55:44 UTC</td>
<td class="timeago" data-time="2021-05-05T16:55:44+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4089195188964218634" rel="nofollow">4089195188964218634</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 May 2021 – 19:46:52 UTC</td>
<td class="timeago" data-time="2021-05-04T19:46:52+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7790512535382270584" rel="nofollow">7790512535382270584</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">1 May 2021 – 16:17:42 UTC</td>
<td class="timeago" data-time="2021-05-01T16:17:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4413694557604739659" rel="nofollow">4413694557604739659</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 April 2021 – 12:21:50 UTC</td>
<td class="timeago" data-time="2021-04-30T12:21:50+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:362252703997605585" rel="nofollow">362252703997605585</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 April 2021 – 00:27:33 UTC</td>
<td class="timeago" data-time="2021-04-30T00:27:33+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4363642205868219010" rel="nofollow">4363642205868219010</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">29 April 2021 – 20:47:09 UTC</td>
<td class="timeago" data-time="2021-04-29T20:47:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3795196318807243288" rel="nofollow">3795196318807243288</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 April 2021 – 21:40:11 UTC</td>
<td class="timeago" data-time="2021-04-27T21:40:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8985348761116827551" rel="nofollow">8985348761116827551</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 April 2021 – 00:56:01 UTC</td>
<td class="timeago" data-time="2021-04-27T00:56:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7038971917761719203" rel="nofollow">7038971917761719203</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">26 April 2021 – 22:08:30 UTC</td>
<td class="timeago" data-time="2021-04-26T22:08:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3993225027000924086" rel="nofollow">3993225027000924086</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 April 2021 – 22:36:59 UTC</td>
<td class="timeago" data-time="2021-04-25T22:36:59+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1059858089546059381" rel="nofollow">1059858089546059381</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 April 2021 – 20:27:35 UTC</td>
<td class="timeago" data-time="2021-04-25T20:27:35+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4337065418277532998" rel="nofollow">4337065418277532998</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 April 2021 – 22:32:23 UTC</td>
<td class="timeago" data-time="2021-04-24T22:32:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7294046835606537349" rel="nofollow">7294046835606537349</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 April 2021 – 18:22:41 UTC</td>
<td class="timeago" data-time="2021-04-24T18:22:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1196079393968860562" rel="nofollow">1196079393968860562</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 March 2021 – 17:11:12 UTC</td>
<td class="timeago" data-time="2021-03-27T17:11:12+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2614264348337776299" rel="nofollow">2614264348337776299</a>
</td>
</tr>
<tr>
<td class="text-right">23 March 2021 – 16:25:32 UTC</td>
<td class="timeago" data-time="2021-03-23T16:25:32+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2889825603929698068" rel="nofollow">2889825603929698068</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 March 2021 – 00:52:47 UTC</td>
<td class="timeago" data-time="2021-03-23T00:52:47+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3526208138514740690" rel="nofollow">3526208138514740690</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 March 2021 – 19:58:12 UTC</td>
<td class="timeago" data-time="2021-03-21T19:58:12+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2048232362729735779" rel="nofollow">2048232362729735779</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">20 March 2021 – 22:09:41 UTC</td>
<td class="timeago" data-time="2021-03-20T22:09:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2672393779310480253" rel="nofollow">2672393779310480253</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">19 March 2021 – 22:45:10 UTC</td>
<td class="timeago" data-time="2021-03-19T22:45:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6325173276974416834" rel="nofollow">6325173276974416834</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">19 March 2021 – 03:25:56 UTC</td>
<td class="timeago" data-time="2021-03-19T03:25:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1328663041342885995" rel="nofollow">1328663041342885995</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 March 2021 – 23:01:13 UTC</td>
<td class="timeago" data-time="2021-03-18T23:01:13+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2379777614176168862" rel="nofollow">2379777614176168862</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 March 2021 – 18:23:19 UTC</td>
<td class="timeago" data-time="2021-03-18T18:23:19+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4168816630673080410" rel="nofollow">4168816630673080410</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">6 March 2021 – 18:42:25 UTC</td>
<td class="timeago" data-time="2021-03-06T18:42:25+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1956167462642507037" rel="nofollow">1956167462642507037</a>
</td>
</tr>
<tr>
<td class="text-right">3 March 2021 – 21:05:03 UTC</td>
<td class="timeago" data-time="2021-03-03T21:05:03+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7821275763370713096" rel="nofollow">7821275763370713096</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 March 2021 – 19:07:41 UTC</td>
<td class="timeago" data-time="2021-03-03T19:07:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2814330753528914935" rel="nofollow">2814330753528914935</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 March 2021 – 19:48:52 UTC</td>
<td class="timeago" data-time="2021-03-02T19:48:52+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8167630516751842762" rel="nofollow">8167630516751842762</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 February 2021 – 20:55:12 UTC</td>
<td class="timeago" data-time="2021-02-28T20:55:12+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5707957810573856881" rel="nofollow">5707957810573856881</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 February 2021 – 01:52:13 UTC</td>
<td class="timeago" data-time="2021-02-28T01:52:13+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3774413373752896786" rel="nofollow">3774413373752896786</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 February 2021 – 19:07:51 UTC</td>
<td class="timeago" data-time="2021-02-27T19:07:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2099743558686489587" rel="nofollow">2099743558686489587</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">26 February 2021 – 17:30:10 UTC</td>
<td class="timeago" data-time="2021-02-26T17:30:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2415015908938182036" rel="nofollow">2415015908938182036</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 February 2021 – 23:23:35 UTC</td>
<td class="timeago" data-time="2021-02-25T23:23:35+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2121502761852034088" rel="nofollow">2121502761852034088</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 February 2021 – 20:55:31 UTC</td>
<td class="timeago" data-time="2021-02-25T20:55:31+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4487362956181238684" rel="nofollow">4487362956181238684</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 February 2021 – 01:06:23 UTC</td>
<td class="timeago" data-time="2021-02-25T01:06:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1164881261160089854" rel="nofollow">1164881261160089854</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 February 2021 – 22:46:10 UTC</td>
<td class="timeago" data-time="2021-02-24T22:46:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7967663130782647779" rel="nofollow">7967663130782647779</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">22 February 2021 – 23:31:29 UTC</td>
<td class="timeago" data-time="2021-02-22T23:31:29+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1505552910172773927" rel="nofollow">1505552910172773927</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 February 2021 – 23:13:15 UTC</td>
<td class="timeago" data-time="2021-02-21T23:13:15+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:734921142500005095" rel="nofollow">734921142500005095</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 February 2021 – 23:53:33 UTC</td>
<td class="timeago" data-time="2021-02-18T23:53:33+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:583654044159578421" rel="nofollow">583654044159578421</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">17 February 2021 – 23:02:14 UTC</td>
<td class="timeago" data-time="2021-02-17T23:02:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2896491024285117197" rel="nofollow">2896491024285117197</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">15 February 2021 – 00:24:19 UTC</td>
<td class="timeago" data-time="2021-02-15T00:24:19+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3409678201917773821" rel="nofollow">3409678201917773821</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">14 February 2021 – 16:21:42 UTC</td>
<td class="timeago" data-time="2021-02-14T16:21:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:65236652974726321" rel="nofollow">65236652974726321</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">13 February 2021 – 19:21:56 UTC</td>
<td class="timeago" data-time="2021-02-13T19:21:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8848012567107943644" rel="nofollow">8848012567107943644</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">13 February 2021 – 17:21:49 UTC</td>
<td class="timeago" data-time="2021-02-13T17:21:49+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1515698465907472354" rel="nofollow">1515698465907472354</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 February 2021 – 13:54:04 UTC</td>
<td class="timeago" data-time="2021-02-12T13:54:04+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2858874397181780085" rel="nofollow">2858874397181780085</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">10 February 2021 – 23:38:28 UTC</td>
<td class="timeago" data-time="2021-02-10T23:38:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3532338698815106964" rel="nofollow">3532338698815106964</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">9 February 2021 – 21:52:32 UTC</td>
<td class="timeago" data-time="2021-02-09T21:52:32+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9010258389075557648" rel="nofollow">9010258389075557648</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">8 February 2021 – 18:13:56 UTC</td>
<td class="timeago" data-time="2021-02-08T18:13:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2781219300908174901" rel="nofollow">2781219300908174901</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 February 2021 – 21:51:33 UTC</td>
<td class="timeago" data-time="2021-02-07T21:51:33+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3803839957344111197" rel="nofollow">3803839957344111197</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 February 2021 – 19:44:24 UTC</td>
<td class="timeago" data-time="2021-02-07T19:44:24+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3381371473951962084" rel="nofollow">3381371473951962084</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">5 February 2021 – 19:07:58 UTC</td>
<td class="timeago" data-time="2021-02-05T19:07:58+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7220509654981624697" rel="nofollow">7220509654981624697</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 February 2021 – 21:54:05 UTC</td>
<td class="timeago" data-time="2021-02-04T21:54:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1725653230078071359" rel="nofollow">1725653230078071359</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 February 2021 – 21:08:01 UTC</td>
<td class="timeago" data-time="2021-02-03T21:08:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5697277420499534131" rel="nofollow">5697277420499534131</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">1 February 2021 – 23:56:52 UTC</td>
<td class="timeago" data-time="2021-02-01T23:56:52+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:307902514686226458" rel="nofollow">307902514686226458</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">1 February 2021 – 21:51:07 UTC</td>
<td class="timeago" data-time="2021-02-01T21:51:07+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5324193759544630625" rel="nofollow">5324193759544630625</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">31 January 2021 – 21:41:54 UTC</td>
<td class="timeago" data-time="2021-01-31T21:41:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6874318584933089610" rel="nofollow">6874318584933089610</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 January 2021 – 16:42:53 UTC</td>
<td class="timeago" data-time="2021-01-30T16:42:53+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6280538217764533822" rel="nofollow">6280538217764533822</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">29 January 2021 – 18:27:56 UTC</td>
<td class="timeago" data-time="2021-01-29T18:27:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6041425839377909012" rel="nofollow">6041425839377909012</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 January 2021 – 20:54:37 UTC</td>
<td class="timeago" data-time="2021-01-28T20:54:37+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:493680007711147313" rel="nofollow">493680007711147313</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 January 2021 – 22:14:07 UTC</td>
<td class="timeago" data-time="2021-01-27T22:14:07+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1212213843857930052" rel="nofollow">1212213843857930052</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 January 2021 – 19:32:03 UTC</td>
<td class="timeago" data-time="2021-01-27T19:32:03+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6221467766756910687" rel="nofollow">6221467766756910687</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 January 2021 – 18:17:13 UTC</td>
<td class="timeago" data-time="2021-01-27T18:17:13+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4116228448230303743" rel="nofollow">4116228448230303743</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">26 January 2021 – 17:03:50 UTC</td>
<td class="timeago" data-time="2021-01-26T17:03:50+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4136143701261008556" rel="nofollow">4136143701261008556</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">26 January 2021 – 15:10:40 UTC</td>
<td class="timeago" data-time="2021-01-26T15:10:40+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3630920264960804677" rel="nofollow">3630920264960804677</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 January 2021 – 21:26:38 UTC</td>
<td class="timeago" data-time="2021-01-24T21:26:38+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4017804763582095674" rel="nofollow">4017804763582095674</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 January 2021 – 01:21:07 UTC</td>
<td class="timeago" data-time="2021-01-23T01:21:07+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8567498548737690498" rel="nofollow">8567498548737690498</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 January 2021 – 00:13:18 UTC</td>
<td class="timeago" data-time="2021-01-23T00:13:18+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8577854876931197867" rel="nofollow">8577854876931197867</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 January 2021 – 20:56:59 UTC</td>
<td class="timeago" data-time="2021-01-21T20:56:59+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1541680551006752692" rel="nofollow">1541680551006752692</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">19 January 2021 – 21:39:46 UTC</td>
<td class="timeago" data-time="2021-01-19T21:39:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5900292383059526441" rel="nofollow">5900292383059526441</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">19 January 2021 – 17:29:45 UTC</td>
<td class="timeago" data-time="2021-01-19T17:29:45+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1718462879070703041" rel="nofollow">1718462879070703041</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 January 2021 – 18:00:48 UTC</td>
<td class="timeago" data-time="2021-01-18T18:00:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2233203074140638058" rel="nofollow">2233203074140638058</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">17 January 2021 – 18:20:10 UTC</td>
<td class="timeago" data-time="2021-01-17T18:20:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5244079320564391994" rel="nofollow">5244079320564391994</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">16 January 2021 – 19:24:18 UTC</td>
<td class="timeago" data-time="2021-01-16T19:24:18+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1896793525347305467" rel="nofollow">1896793525347305467</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">16 January 2021 – 00:37:02 UTC</td>
<td class="timeago" data-time="2021-01-16T00:37:02+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1336376144186235216" rel="nofollow">1336376144186235216</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">15 January 2021 – 01:08:31 UTC</td>
<td class="timeago" data-time="2021-01-15T01:08:31+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5790095611891363572" rel="nofollow">5790095611891363572</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">14 January 2021 – 23:50:41 UTC</td>
<td class="timeago" data-time="2021-01-14T23:50:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:472442624629817069" rel="nofollow">472442624629817069</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">14 January 2021 – 21:26:16 UTC</td>
<td class="timeago" data-time="2021-01-14T21:26:16+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:430433914191312395" rel="nofollow">430433914191312395</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 January 2021 – 23:03:15 UTC</td>
<td class="timeago" data-time="2021-01-12T23:03:15+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:110715827455430053" rel="nofollow">110715827455430053</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 January 2021 – 18:34:43 UTC</td>
<td class="timeago" data-time="2021-01-12T18:34:43+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3212159241772543639" rel="nofollow">3212159241772543639</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 January 2021 – 14:58:46 UTC</td>
<td class="timeago" data-time="2021-01-11T14:58:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4637745267672855255" rel="nofollow">4637745267672855255</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">10 January 2021 – 20:22:51 UTC</td>
<td class="timeago" data-time="2021-01-10T20:22:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7144880866023263799" rel="nofollow">7144880866023263799</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">8 January 2021 – 20:23:01 UTC</td>
<td class="timeago" data-time="2021-01-08T20:23:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:113580295176448705" rel="nofollow">113580295176448705</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">8 January 2021 – 17:37:05 UTC</td>
<td class="timeago" data-time="2021-01-08T17:37:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3529893060308761789" rel="nofollow">3529893060308761789</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 January 2021 – 15:51:44 UTC</td>
<td class="timeago" data-time="2021-01-02T15:51:44+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2892448355948705963" rel="nofollow">2892448355948705963</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 December 2020 – 16:51:46 UTC</td>
<td class="timeago" data-time="2020-12-28T16:51:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7511662506100823531" rel="nofollow">7511662506100823531</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">22 December 2020 – 15:08:26 UTC</td>
<td class="timeago" data-time="2020-12-22T15:08:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2788818255460701356" rel="nofollow">2788818255460701356</a>
</td>
</tr>
<tr>
<td class="text-right">18 December 2020 – 18:35:48 UTC</td>
<td class="timeago" data-time="2020-12-18T18:35:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8496242656308167130" rel="nofollow">8496242656308167130</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 December 2020 – 15:08:42 UTC</td>
<td class="timeago" data-time="2020-12-18T15:08:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:953292077313283689" rel="nofollow">953292077313283689</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 December 2020 – 16:00:26 UTC</td>
<td class="timeago" data-time="2020-12-11T16:00:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6670187091170116752" rel="nofollow">6670187091170116752</a>
</td>
</tr>
<tr>
<td class="text-right">10 December 2020 – 18:39:23 UTC</td>
<td class="timeago" data-time="2020-12-10T18:39:23+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7452889000998778089" rel="nofollow">7452889000998778089</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">9 December 2020 – 16:41:48 UTC</td>
<td class="timeago" data-time="2020-12-09T16:41:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:49154117056968789" rel="nofollow">49154117056968789</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">8 December 2020 – 19:12:00 UTC</td>
<td class="timeago" data-time="2020-12-08T19:12:00+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8444216083477085344" rel="nofollow">8444216083477085344</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 December 2020 – 02:34:20 UTC</td>
<td class="timeago" data-time="2020-12-07T02:34:20+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5154984155740013556" rel="nofollow">5154984155740013556</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 December 2020 – 00:22:46 UTC</td>
<td class="timeago" data-time="2020-12-07T00:22:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3176164837032318208" rel="nofollow">3176164837032318208</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">5 December 2020 – 19:39:02 UTC</td>
<td class="timeago" data-time="2020-12-05T19:39:02+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7091595905540317051" rel="nofollow">7091595905540317051</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 December 2020 – 00:00:17 UTC</td>
<td class="timeago" data-time="2020-12-04T00:00:17+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8020151335569137463" rel="nofollow">8020151335569137463</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 December 2020 – 23:35:26 UTC</td>
<td class="timeago" data-time="2020-12-02T23:35:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7445196959152614867" rel="nofollow">7445196959152614867</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">29 November 2020 – 21:10:48 UTC</td>
<td class="timeago" data-time="2020-11-29T21:10:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5662080582243562643" rel="nofollow">5662080582243562643</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 November 2020 – 20:56:15 UTC</td>
<td class="timeago" data-time="2020-11-28T20:56:15+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:156114923659761104" rel="nofollow">156114923659761104</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 November 2020 – 14:56:10 UTC</td>
<td class="timeago" data-time="2020-11-28T14:56:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:620558228550564040" rel="nofollow">620558228550564040</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">9 November 2020 – 18:05:01 UTC</td>
<td class="timeago" data-time="2020-11-09T18:05:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:257572815972847564" rel="nofollow">257572815972847564</a>
</td>
</tr>
<tr>
<td class="text-right">8 November 2020 – 16:24:56 UTC</td>
<td class="timeago" data-time="2020-11-08T16:24:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5343723663709598366" rel="nofollow">5343723663709598366</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 November 2020 – 23:57:14 UTC</td>
<td class="timeago" data-time="2020-11-07T23:57:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1778334134400807351" rel="nofollow">1778334134400807351</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 November 2020 – 15:42:06 UTC</td>
<td class="timeago" data-time="2020-11-07T15:42:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5530585677262894613" rel="nofollow">5530585677262894613</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">5 November 2020 – 16:30:49 UTC</td>
<td class="timeago" data-time="2020-11-05T16:30:49+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2956971579553407458" rel="nofollow">2956971579553407458</a>
</td>
</tr>
<tr>
<td class="text-right">4 November 2020 – 22:23:11 UTC</td>
<td class="timeago" data-time="2020-11-04T22:23:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4557321508918583131" rel="nofollow">4557321508918583131</a>
</td>
</tr>
<tr>
<td class="text-right">4 November 2020 – 21:43:02 UTC</td>
<td class="timeago" data-time="2020-11-04T21:43:02+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9111647191749720633" rel="nofollow">9111647191749720633</a>
</td>
</tr>
<tr>
<td class="text-right">4 November 2020 – 20:24:09 UTC</td>
<td class="timeago" data-time="2020-11-04T20:24:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8941398836450497180" rel="nofollow">8941398836450497180</a>
</td>
</tr>
<tr>
<td class="text-right">4 November 2020 – 17:19:47 UTC</td>
<td class="timeago" data-time="2020-11-04T17:19:47+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4759647009991346290" rel="nofollow">4759647009991346290</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 November 2020 – 17:56:21 UTC</td>
<td class="timeago" data-time="2020-11-03T17:56:21+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9034869613024820206" rel="nofollow">9034869613024820206</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 November 2020 – 23:15:57 UTC</td>
<td class="timeago" data-time="2020-11-02T23:15:57+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:71921842228051739" rel="nofollow">71921842228051739</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 November 2020 – 18:07:42 UTC</td>
<td class="timeago" data-time="2020-11-02T18:07:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1752303990270177264" rel="nofollow">1752303990270177264</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 November 2020 – 14:28:11 UTC</td>
<td class="timeago" data-time="2020-11-02T14:28:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3050252166013825884" rel="nofollow">3050252166013825884</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">2 November 2020 – 00:52:51 UTC</td>
<td class="timeago" data-time="2020-11-02T00:52:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1615075213601662923" rel="nofollow">1615075213601662923</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">1 November 2020 – 22:53:34 UTC</td>
<td class="timeago" data-time="2020-11-01T22:53:34+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5809777791656599166" rel="nofollow">5809777791656599166</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">1 November 2020 – 17:25:36 UTC</td>
<td class="timeago" data-time="2020-11-01T17:25:36+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3585368477341146624" rel="nofollow">3585368477341146624</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">31 October 2020 – 20:21:14 UTC</td>
<td class="timeago" data-time="2020-10-31T20:21:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5603350045680984288" rel="nofollow">5603350045680984288</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">31 October 2020 – 12:52:07 UTC</td>
<td class="timeago" data-time="2020-10-31T12:52:07+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6403132324717893944" rel="nofollow">6403132324717893944</a>
</td>
</tr>
<tr>
<td class="text-right">30 October 2020 – 18:49:30 UTC</td>
<td class="timeago" data-time="2020-10-30T18:49:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1276987311780876745" rel="nofollow">1276987311780876745</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 October 2020 – 17:00:00 UTC</td>
<td class="timeago" data-time="2020-10-30T17:00:00+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8655268598696966967" rel="nofollow">8655268598696966967</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 October 2020 – 16:12:21 UTC</td>
<td class="timeago" data-time="2020-10-30T16:12:21+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1292121820473944008" rel="nofollow">1292121820473944008</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 October 2020 – 01:47:04 UTC</td>
<td class="timeago" data-time="2020-10-30T01:47:04+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6540397407515988088" rel="nofollow">6540397407515988088</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">29 October 2020 – 23:56:28 UTC</td>
<td class="timeago" data-time="2020-10-29T23:56:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5294455951006820559" rel="nofollow">5294455951006820559</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">29 October 2020 – 14:16:06 UTC</td>
<td class="timeago" data-time="2020-10-29T14:16:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:331554245455913537" rel="nofollow">331554245455913537</a>
</td>
</tr>
<tr>
<td class="text-right">28 October 2020 – 18:51:39 UTC</td>
<td class="timeago" data-time="2020-10-28T18:51:39+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8010101673184951013" rel="nofollow">8010101673184951013</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 October 2020 – 01:44:29 UTC</td>
<td class="timeago" data-time="2020-10-28T01:44:29+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8220182678043697307" rel="nofollow">8220182678043697307</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 October 2020 – 14:09:41 UTC</td>
<td class="timeago" data-time="2020-10-27T14:09:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:133554029231182250" rel="nofollow">133554029231182250</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 October 2020 – 00:34:09 UTC</td>
<td class="timeago" data-time="2020-10-27T00:34:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8866068598634483362" rel="nofollow">8866068598634483362</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">26 October 2020 – 22:38:35 UTC</td>
<td class="timeago" data-time="2020-10-26T22:38:35+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5794670269347856170" rel="nofollow">5794670269347856170</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 October 2020 – 23:57:51 UTC</td>
<td class="timeago" data-time="2020-10-25T23:57:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5419310247515743814" rel="nofollow">5419310247515743814</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 October 2020 – 21:21:25 UTC</td>
<td class="timeago" data-time="2020-10-25T21:21:25+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7577745464313649170" rel="nofollow">7577745464313649170</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 October 2020 – 18:06:01 UTC</td>
<td class="timeago" data-time="2020-10-24T18:06:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6457817926454011815" rel="nofollow">6457817926454011815</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 October 2020 – 21:27:50 UTC</td>
<td class="timeago" data-time="2020-10-23T21:27:50+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5634788777319823704" rel="nofollow">5634788777319823704</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">22 October 2020 – 09:49:46 UTC</td>
<td class="timeago" data-time="2020-10-22T09:49:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8375010256554668971" rel="nofollow">8375010256554668971</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">20 October 2020 – 00:49:42 UTC</td>
<td class="timeago" data-time="2020-10-20T00:49:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5675773480993221153" rel="nofollow">5675773480993221153</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">19 October 2020 – 02:30:05 UTC</td>
<td class="timeago" data-time="2020-10-19T02:30:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4450572876248706235" rel="nofollow">4450572876248706235</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 October 2020 – 23:39:49 UTC</td>
<td class="timeago" data-time="2020-10-18T23:39:49+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2974849544247619646" rel="nofollow">2974849544247619646</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">18 October 2020 – 00:05:54 UTC</td>
<td class="timeago" data-time="2020-10-18T00:05:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8147405631935969774" rel="nofollow">8147405631935969774</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">17 October 2020 – 02:20:56 UTC</td>
<td class="timeago" data-time="2020-10-17T02:20:56+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9105432220852276778" rel="nofollow">9105432220852276778</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">16 October 2020 – 01:22:00 UTC</td>
<td class="timeago" data-time="2020-10-16T01:22:00+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6635670544741844370" rel="nofollow">6635670544741844370</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">15 October 2020 – 23:11:09 UTC</td>
<td class="timeago" data-time="2020-10-15T23:11:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1813097555791828350" rel="nofollow">1813097555791828350</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">13 October 2020 – 21:51:10 UTC</td>
<td class="timeago" data-time="2020-10-13T21:51:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5821355763069196492" rel="nofollow">5821355763069196492</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">13 October 2020 – 00:58:04 UTC</td>
<td class="timeago" data-time="2020-10-13T00:58:04+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2788815784501469633" rel="nofollow">2788815784501469633</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 October 2020 – 21:25:58 UTC</td>
<td class="timeago" data-time="2020-10-12T21:25:58+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5811825097987376059" rel="nofollow">5811825097987376059</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 October 2020 – 02:23:02 UTC</td>
<td class="timeago" data-time="2020-10-12T02:23:02+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2243281498572868231" rel="nofollow">2243281498572868231</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">12 October 2020 – 00:16:46 UTC</td>
<td class="timeago" data-time="2020-10-12T00:16:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5928861263880446455" rel="nofollow">5928861263880446455</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 October 2020 – 17:54:52 UTC</td>
<td class="timeago" data-time="2020-10-11T17:54:52+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5354360636171734776" rel="nofollow">5354360636171734776</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">11 October 2020 – 01:03:46 UTC</td>
<td class="timeago" data-time="2020-10-11T01:03:46+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6952827886477257091" rel="nofollow">6952827886477257091</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">10 October 2020 – 23:56:47 UTC</td>
<td class="timeago" data-time="2020-10-10T23:56:47+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6943554767869515020" rel="nofollow">6943554767869515020</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">10 October 2020 – 22:41:37 UTC</td>
<td class="timeago" data-time="2020-10-10T22:41:37+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2413543430396853277" rel="nofollow">2413543430396853277</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">10 October 2020 – 02:04:29 UTC</td>
<td class="timeago" data-time="2020-10-10T02:04:29+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9110747829856991011" rel="nofollow">9110747829856991011</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">10 October 2020 – 00:41:10 UTC</td>
<td class="timeago" data-time="2020-10-10T00:41:10+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9113419214534785698" rel="nofollow">9113419214534785698</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">9 October 2020 – 23:30:53 UTC</td>
<td class="timeago" data-time="2020-10-09T23:30:53+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8351664103236215898" rel="nofollow">8351664103236215898</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">8 October 2020 – 23:18:30 UTC</td>
<td class="timeago" data-time="2020-10-08T23:18:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1311494234730820187" rel="nofollow">1311494234730820187</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">8 October 2020 – 21:41:16 UTC</td>
<td class="timeago" data-time="2020-10-08T21:41:16+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5908350036487099694" rel="nofollow">5908350036487099694</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 October 2020 – 23:22:38 UTC</td>
<td class="timeago" data-time="2020-10-07T23:22:38+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7057946416338031944" rel="nofollow">7057946416338031944</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">7 October 2020 – 01:20:42 UTC</td>
<td class="timeago" data-time="2020-10-07T01:20:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9140611648240214395" rel="nofollow">9140611648240214395</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">6 October 2020 – 20:47:48 UTC</td>
<td class="timeago" data-time="2020-10-06T20:47:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7048470024745291371" rel="nofollow">7048470024745291371</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">6 October 2020 – 18:23:35 UTC</td>
<td class="timeago" data-time="2020-10-06T18:23:35+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6847780632202387993" rel="nofollow">6847780632202387993</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">6 October 2020 – 17:18:33 UTC</td>
<td class="timeago" data-time="2020-10-06T17:18:33+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4654695157832577197" rel="nofollow">4654695157832577197</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">5 October 2020 – 23:19:35 UTC</td>
<td class="timeago" data-time="2020-10-05T23:19:35+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7005233772418205478" rel="nofollow">7005233772418205478</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">5 October 2020 – 17:29:16 UTC</td>
<td class="timeago" data-time="2020-10-05T17:29:16+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1089162639368818063" rel="nofollow">1089162639368818063</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 22:03:50 UTC</td>
<td class="timeago" data-time="2020-10-04T22:03:50+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4488252479481708564" rel="nofollow">4488252479481708564</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 19:38:31 UTC</td>
<td class="timeago" data-time="2020-10-04T19:38:31+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5140012035067730938" rel="nofollow">5140012035067730938</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 17:02:11 UTC</td>
<td class="timeago" data-time="2020-10-04T17:02:11+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8215728223290007202" rel="nofollow">8215728223290007202</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 13:47:14 UTC</td>
<td class="timeago" data-time="2020-10-04T13:47:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5582552730957699088" rel="nofollow">5582552730957699088</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 03:01:26 UTC</td>
<td class="timeago" data-time="2020-10-04T03:01:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7362394472291673156" rel="nofollow">7362394472291673156</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 02:03:29 UTC</td>
<td class="timeago" data-time="2020-10-04T02:03:29+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6045928462402827528" rel="nofollow">6045928462402827528</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">4 October 2020 – 00:25:30 UTC</td>
<td class="timeago" data-time="2020-10-04T00:25:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5617247296057855455" rel="nofollow">5617247296057855455</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 October 2020 – 23:26:09 UTC</td>
<td class="timeago" data-time="2020-10-03T23:26:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:316070239507377538" rel="nofollow">316070239507377538</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 October 2020 – 19:31:40 UTC</td>
<td class="timeago" data-time="2020-10-03T19:31:40+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2746501647516536714" rel="nofollow">2746501647516536714</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 October 2020 – 17:27:17 UTC</td>
<td class="timeago" data-time="2020-10-03T17:27:17+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5331135907407000399" rel="nofollow">5331135907407000399</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 October 2020 – 01:51:47 UTC</td>
<td class="timeago" data-time="2020-10-03T01:51:47+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7751803146642549318" rel="nofollow">7751803146642549318</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">3 October 2020 – 00:07:47 UTC</td>
<td class="timeago" data-time="2020-10-03T00:07:47+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6730938097469079113" rel="nofollow">6730938097469079113</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 September 2020 – 20:05:48 UTC</td>
<td class="timeago" data-time="2020-09-30T20:05:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2393199652183266332" rel="nofollow">2393199652183266332</a>
</td>
</tr>
<tr>
<td class="text-right">30 September 2020 – 18:00:06 UTC</td>
<td class="timeago" data-time="2020-09-30T18:00:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7268144294140291567" rel="nofollow">7268144294140291567</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">30 September 2020 – 02:48:14 UTC</td>
<td class="timeago" data-time="2020-09-30T02:48:14+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6309368592595771124" rel="nofollow">6309368592595771124</a>
</td>
</tr>
<tr>
<td class="text-right">29 September 2020 – 22:26:43 UTC</td>
<td class="timeago" data-time="2020-09-29T22:26:43+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1733179039752492430" rel="nofollow">1733179039752492430</a>
</td>
</tr>
<tr>
<td class="text-right">29 September 2020 – 02:20:42 UTC</td>
<td class="timeago" data-time="2020-09-29T02:20:42+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:77266022982840487" rel="nofollow">77266022982840487</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">28 September 2020 – 19:25:29 UTC</td>
<td class="timeago" data-time="2020-09-28T19:25:29+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3104982974508925454" rel="nofollow">3104982974508925454</a>
</td>
</tr>
<tr>
<td class="text-right">28 September 2020 – 17:38:51 UTC</td>
<td class="timeago" data-time="2020-09-28T17:38:51+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2728443211707891570" rel="nofollow">2728443211707891570</a>
</td>
</tr>
<tr>
<td class="text-right">28 September 2020 – 16:54:45 UTC</td>
<td class="timeago" data-time="2020-09-28T16:54:45+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4301340284486913253" rel="nofollow">4301340284486913253</a>
</td>
</tr>
<tr>
<td class="text-right">27 September 2020 – 18:58:01 UTC</td>
<td class="timeago" data-time="2020-09-27T18:58:01+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5474001979451045934" rel="nofollow">5474001979451045934</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">27 September 2020 – 12:46:25 UTC</td>
<td class="timeago" data-time="2020-09-27T12:46:25+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:813702279420185490" rel="nofollow">813702279420185490</a>
</td>
</tr>
<tr>
<td class="text-right">26 September 2020 – 20:00:36 UTC</td>
<td class="timeago" data-time="2020-09-26T20:00:36+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4019199694333068191" rel="nofollow">4019199694333068191</a>
</td>
</tr>
<tr>
<td class="text-right">26 September 2020 – 17:50:54 UTC</td>
<td class="timeago" data-time="2020-09-26T17:50:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4840185609462223586" rel="nofollow">4840185609462223586</a>
</td>
</tr>
<tr>
<td class="text-right">26 September 2020 – 13:23:05 UTC</td>
<td class="timeago" data-time="2020-09-26T13:23:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:9047602742621251185" rel="nofollow">9047602742621251185</a>
</td>
</tr>
<tr>
<td class="text-right">26 September 2020 – 04:43:18 UTC</td>
<td class="timeago" data-time="2020-09-26T04:43:18+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1886012288923231336" rel="nofollow">1886012288923231336</a>
</td>
</tr>
<tr>
<td class="text-right">26 September 2020 – 03:14:43 UTC</td>
<td class="timeago" data-time="2020-09-26T03:14:43+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1798744823145507234" rel="nofollow">1798744823145507234</a>
</td>
</tr>
<tr>
<td class="text-right">25 September 2020 – 20:58:30 UTC</td>
<td class="timeago" data-time="2020-09-25T20:58:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3770780936132666057" rel="nofollow">3770780936132666057</a>
</td>
</tr>
<tr>
<td class="text-right">25 September 2020 – 19:09:39 UTC</td>
<td class="timeago" data-time="2020-09-25T19:09:39+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5736808859437447356" rel="nofollow">5736808859437447356</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">25 September 2020 – 05:16:33 UTC</td>
<td class="timeago" data-time="2020-09-25T05:16:33+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5605500816342086763" rel="nofollow">5605500816342086763</a>
</td>
</tr>
<tr>
<td class="text-right">25 September 2020 – 02:21:48 UTC</td>
<td class="timeago" data-time="2020-09-25T02:21:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:817375777744422496" rel="nofollow">817375777744422496</a>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 22:09:41 UTC</td>
<td class="timeago" data-time="2020-09-24T22:09:41+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1413850815597817360" rel="nofollow">1413850815597817360</a>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 20:08:48 UTC</td>
<td class="timeago" data-time="2020-09-24T20:08:48+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7268665984080507595" rel="nofollow">7268665984080507595</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 19:26:54 UTC</td>
<td class="timeago" data-time="2020-09-24T19:26:54+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8287605472402055500" rel="nofollow">8287605472402055500</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 18:20:15 UTC</td>
<td class="timeago" data-time="2020-09-24T18:20:15+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1417993155064019530" rel="nofollow">1417993155064019530</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 15:48:24 UTC</td>
<td class="timeago" data-time="2020-09-24T15:48:24+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:7621547092877068091" rel="nofollow">7621547092877068091</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 04:01:27 UTC</td>
<td class="timeago" data-time="2020-09-24T04:01:27+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:287112752107517027" rel="nofollow">287112752107517027</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">24 September 2020 – 00:52:57 UTC</td>
<td class="timeago" data-time="2020-09-24T00:52:57+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1929506470584439525" rel="nofollow">1929506470584439525</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 September 2020 – 23:40:06 UTC</td>
<td class="timeago" data-time="2020-09-23T23:40:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6032140682415529513" rel="nofollow">6032140682415529513</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 September 2020 – 22:30:22 UTC</td>
<td class="timeago" data-time="2020-09-23T22:30:22+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:403083281573097975" rel="nofollow">403083281573097975</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">23 September 2020 – 02:14:26 UTC</td>
<td class="timeago" data-time="2020-09-23T02:14:26+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4613042581869599070" rel="nofollow">4613042581869599070</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">22 September 2020 – 16:39:05 UTC</td>
<td class="timeago" data-time="2020-09-22T16:39:05+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5474961254698819968" rel="nofollow">5474961254698819968</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">22 September 2020 – 03:16:31 UTC</td>
<td class="timeago" data-time="2020-09-22T03:16:31+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1400850317024274774" rel="nofollow">1400850317024274774</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">22 September 2020 – 02:45:13 UTC</td>
<td class="timeago" data-time="2020-09-22T02:45:13+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6563733616859568570" rel="nofollow">6563733616859568570</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 September 2020 – 22:50:28 UTC</td>
<td class="timeago" data-time="2020-09-21T22:50:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4459459451674349131" rel="nofollow">4459459451674349131</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 September 2020 – 21:04:57 UTC</td>
<td class="timeago" data-time="2020-09-21T21:04:57+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8400613947673468740" rel="nofollow">8400613947673468740</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 September 2020 – 03:21:16 UTC</td>
<td class="timeago" data-time="2020-09-21T03:21:16+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2385705787862808228" rel="nofollow">2385705787862808228</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 September 2020 – 02:50:38 UTC</td>
<td class="timeago" data-time="2020-09-21T02:50:38+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1316115866753937312" rel="nofollow">1316115866753937312</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 September 2020 – 02:11:58 UTC</td>
<td class="timeago" data-time="2020-09-21T02:11:58+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:477468889012811775" rel="nofollow">477468889012811775</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">21 September 2020 – 00:26:38 UTC</td>
<td class="timeago" data-time="2020-09-21T00:26:38+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8845503200875600806" rel="nofollow">8845503200875600806</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">20 September 2020 – 22:07:40 UTC</td>
<td class="timeago" data-time="2020-09-20T22:07:40+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1144915671495307231" rel="nofollow">1144915671495307231</a>
<code class="js-branch">beta</code>
</td>
</tr>
<tr>
<td class="text-right">20 September 2020 – 03:57:40 UTC</td>
<td class="timeago" data-time="2020-09-20T03:57:40+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:1809119953497934757" rel="nofollow">1809119953497934757</a>
</td>
</tr>
<tr>
<td class="text-right">20 September 2020 – 02:38:28 UTC</td>
<td class="timeago" data-time="2020-09-20T02:38:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6347641551945242118" rel="nofollow">6347641551945242118</a>
</td>
</tr>
<tr>
<td class="text-right">19 September 2020 – 21:15:30 UTC</td>
<td class="timeago" data-time="2020-09-19T21:15:30+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:8366349962366585243" rel="nofollow">8366349962366585243</a>
</td>
</tr>
<tr>
<td class="text-right">19 September 2020 – 15:04:22 UTC</td>
<td class="timeago" data-time="2020-09-19T15:04:22+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6534308844318570309" rel="nofollow">6534308844318570309</a>
</td>
</tr>
<tr>
<td class="text-right">19 September 2020 – 12:42:22 UTC</td>
<td class="timeago" data-time="2020-09-19T12:42:22+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4906545253810991700" rel="nofollow">4906545253810991700</a>
</td>
</tr>
<tr>
<td class="text-right">19 September 2020 – 08:22:09 UTC</td>
<td class="timeago" data-time="2020-09-19T08:22:09+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3469924057916577229" rel="nofollow">3469924057916577229</a>
</td>
</tr>
<tr>
<td class="text-right">19 September 2020 – 02:26:07 UTC</td>
<td class="timeago" data-time="2020-09-19T02:26:07+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:642299258744791023" rel="nofollow">642299258744791023</a>
</td>
</tr>
<tr>
<td class="text-right">18 September 2020 – 13:17:57 UTC</td>
<td class="timeago" data-time="2020-09-18T13:17:57+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:6268849054597914136" rel="nofollow">6268849054597914136</a>
</td>
</tr>
<tr>
<td class="text-right">17 September 2020 – 15:45:06 UTC</td>
<td class="timeago" data-time="2020-09-17T15:45:06+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3133504926118863136" rel="nofollow">3133504926118863136</a>
</td>
</tr>
<tr>
<td class="text-right">17 September 2020 – 14:01:28 UTC</td>
<td class="timeago" data-time="2020-09-17T14:01:28+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:3525096965699228483" rel="nofollow">3525096965699228483</a>
</td>
</tr>
<tr>
<td class="text-right">17 September 2020 – 12:28:29 UTC</td>
<td class="timeago" data-time="2020-09-17T12:28:29+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:5151905135648468514" rel="nofollow">5151905135648468514</a>
</td>
</tr>
<tr>
<td class="text-right">16 September 2020 – 20:54:44 UTC</td>
<td class="timeago" data-time="2020-09-16T20:54:44+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:212675436551312683" rel="nofollow">212675436551312683</a>
</td>
</tr>
<tr>
<td class="text-right">15 September 2020 – 17:35:07 UTC</td>
<td class="timeago" data-time="2020-09-15T17:35:07+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:4530135598969683128" rel="nofollow">4530135598969683128</a>
</td>
</tr>
<tr>
<td class="text-right">14 September 2020 – 18:08:47 UTC</td>
<td class="timeago" data-time="2020-09-14T18:08:47+00:00"> </td>
<td class="tabular-nums">
<a href="/depot/739631/history/?changeid=M:2793946223888382716" rel="nofollow">2793946223888382716</a>
</td>"""

soup = BeautifulSoup(html, 'html.parser')
value = soup.findAll("td", {"class": "text-right"})
value2 = soup.findAll("a", {"rel": "nofollow"})

#for y in value2:
#    manifest = re.findall("[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]", str(y))
#    print(manifest[0])

valueCount = 0

for x in value:
    date = re.findall("[\.0-9]", str(x))
    manifestDate = str(x).replace('<td class="text-right">', "").replace(' UTC</td>', "")
    manifest = re.findall("[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]+[\.0-9]", str(value2[valueCount]))
    manifestVersion = manifest[0]
    valueCount = valueCount + 1
    data = {
        "date": f"{manifestDate}",
        "manifest": f"{manifestVersion}"
    }
    with open(r'C:\Users\danie\Desktop\manifest.json', 'a') as f:
        f.write(f"""{data},
""")