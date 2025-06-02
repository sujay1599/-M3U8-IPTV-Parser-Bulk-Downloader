import re
import pandas as pd
import os

# Paste your M3U8 content here
full_input_text_extended = """
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/g1bCJEu4joxA2KvvBocojaqUVzz.jpg" group-title="All Series",The 100 S01 E01
http://fortv.cc:8080/series/n7NX45/216258/186674.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/gFmn5m6o9HQnUrVJ7WrdIv8aRDo.jpg" group-title="All Series",The 100 S01 E02
http://fortv.cc:8080/series/n7NX45/216258/186675.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/xEeUZj58SsP2FO6HXVAt07Z52bs.jpg" group-title="All Series",The 100 S01 E03
http://fortv.cc:8080/series/n7NX45/216258/186676.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/cjqfqteWbTlSfQcVfX6E8eQvFlN.jpg" group-title="All Series",The 100 S01 E04
http://fortv.cc:8080/series/n7NX45/216258/186677.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/7QOF7DF6ThqLziyc0OHSl0INuUd.jpg" group-title="All Series",The 100 S01 E05
http://fortv.cc:8080/series/n7NX45/216258/186678.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ywvIK9V7oyZlc9Cw4yBIemgStHm.jpg" group-title="All Series",The 100 S01 E06
http://fortv.cc:8080/series/n7NX45/216258/186679.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/70RkU7wutbo320rjZAdJk2zkTAs.jpg" group-title="All Series",The 100 S01 E07
http://fortv.cc:8080/series/n7NX45/216258/186680.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/9sbZaLgSL8dSCxP8cZzVnoUR6h4.jpg" group-title="All Series",The 100 S01 E08
http://fortv.cc:8080/series/n7NX45/216258/186681.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/oxB6THWezq1zxKcYevcwmxddvZG.jpg" group-title="All Series",The 100 S01 E09
http://fortv.cc:8080/series/n7NX45/216258/186682.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/fQ6pnHaSVsDyzq5H4NHA4h9HtPZ.jpg" group-title="All Series",The 100 S01 E10
http://fortv.cc:8080/series/n7NX45/216258/186683.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/sI1Sr6oOleCrk4pwaa7zifOCo1.jpg" group-title="All Series",The 100 S01 E11
http://fortv.cc:8080/series/n7NX45/216258/186684.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/u2TRn2R3D3cFhERtzeMcA8kfaFb.jpg" group-title="All Series",The 100 S01 E12
http://fortv.cc:8080/series/n7NX45/216258/186685.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S01 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/j9Bj0pjUgRLW6MW7j8CJPoGj2Wi.jpg" group-title="All Series",The 100 S01 E13
http://fortv.cc:8080/series/n7NX45/216258/186686.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/io7d2vXzkFQDkuJkvZf7QRPbsWr.jpg" group-title="All Series",The 100 S02 E01
http://fortv.cc:8080/series/n7NX45/216258/186687.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ke2QIHsaWb5qJI4KugXvGPTK7qu.jpg" group-title="All Series",The 100 S02 E02
http://fortv.cc:8080/series/n7NX45/216258/186688.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ahKCwbOOrlxKTU7MPMZrjWe442N.jpg" group-title="All Series",The 100 S02 E03
http://fortv.cc:8080/series/n7NX45/216258/186689.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/1PO2x0Tc5Qk2vihMHkrewwvk5PS.jpg" group-title="All Series",The 100 S02 E04
http://fortv.cc:8080/series/n7NX45/216258/186690.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ts8QTzD4H6mpCbaH5c5lsgiJqP2.jpg" group-title="All Series",The 100 S02 E05
http://fortv.cc:8080/series/n7NX45/216258/186691.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/dIN13YP9z4yUl8LfLuVSQp9MBW5.jpg" group-title="All Series",The 100 S02 E06
http://fortv.cc:8080/series/n7NX45/216258/186692.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/3qqi6dwKyUHqowyfR3lQhSFOphB.jpg" group-title="All Series",The 100 S02 E07
http://fortv.cc:8080/series/n7NX45/216258/186693.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/yYNgjuYHDJ8ZU929S96FZc2X2Af.jpg" group-title="All Series",The 100 S02 E08
http://fortv.cc:8080/series/n7NX45/216258/186694.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/f4njZlqWLYXE7qEZcw0HHMvalbX.jpg" group-title="All Series",The 100 S02 E09
http://fortv.cc:8080/series/n7NX45/216258/186695.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/WA2yAVExj3CaKuu7Hrc4V095EL.jpg" group-title="All Series",The 100 S02 E10
http://fortv.cc:8080/series/n7NX45/216258/186696.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/3UAn0oxAiEuxNfSTpBv0M9iaa8Q.jpg" group-title="All Series",The 100 S02 E11
http://fortv.cc:8080/series/n7NX45/216258/186697.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/6ndineWrMygrfJE9wip435rnCTr.jpg" group-title="All Series",The 100 S02 E12
http://fortv.cc:8080/series/n7NX45/216258/186698.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/6f5hQYlF1fCWUf4bm7IgxcBk8Rx.jpg" group-title="All Series",The 100 S02 E13
http://fortv.cc:8080/series/n7NX45/216258/186699.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E14" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/r6rtRYqayP2M7yELQ1KVNseLIvW.jpg" group-title="All Series",The 100 S02 E14
http://fortv.cc:8080/series/n7NX45/216258/186700.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E15" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/sHqZilPG5T0IYlnBDSPg8sWu5Z6.jpg" group-title="All Series",The 100 S02 E15
http://fortv.cc:8080/series/n7NX45/216258/186701.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S02 E16" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/nBcok8hBlRW4UG9Bx5mrWiUbdD5.jpg" group-title="All Series",The 100 S02 E16
http://fortv.cc:8080/series/n7NX45/216258/186702.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/lvX5DPGYXGpJs0SHMkXIP4BzE6H.jpg" group-title="All Series",The 100 S03 E01
http://fortv.cc:8080/series/n7NX45/216258/186703.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/pma3VaGLIwugRlRs2h9XyJKoEyQ.jpg" group-title="All Series",The 100 S03 E02
http://fortv.cc:8080/series/n7NX45/216258/186704.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/vafq3iTJTraZGND0EOQxgPISlpq.jpg" group-title="All Series",The 100 S03 E03
http://fortv.cc:8080/series/n7NX45/216258/186705.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/1BQWumd9QB11QgfvinpcwuIk63D.jpg" group-title="All Series",The 100 S03 E04
http://fortv.cc:8080/series/n7NX45/216258/186706.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/udKcSE3ZcmKiGtMhYO1jAGOTqV4.jpg" group-title="All Series",The 100 S03 E05
http://fortv.cc:8080/series/n7NX45/216258/186707.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/4QczMxOkAm5c1660sREKgj3Zhsi.jpg" group-title="All Series",The 100 S03 E06
http://fortv.cc:8080/series/n7NX45/216258/186708.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/7Fi9XadAFreytFRYeLZj0QsY2KZ.jpg" group-title="All Series",The 100 S03 E07
http://fortv.cc:8080/series/n7NX45/216258/186709.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/3miP59qiZRslnNFkyFGIhOPDxTY.jpg" group-title="All Series",The 100 S03 E08
http://fortv.cc:8080/series/n7NX45/216258/186710.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/uUo6FG5WwzDkYgg8lafcujsgaMg.jpg" group-title="All Series",The 100 S03 E09
http://fortv.cc:8080/series/n7NX45/216258/186711.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ljlEysgEddN4IoyfYiCP2IlZq0B.jpg" group-title="All Series",The 100 S03 E10
http://fortv.cc:8080/series/n7NX45/216258/186712.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/vIoeTABMZ0mEAhhqifzL1m99n4B.jpg" group-title="All Series",The 100 S03 E11
http://fortv.cc:8080/series/n7NX45/216258/186713.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ykN1FtGGhlIg3BfwOlQgJWo12RJ.jpg" group-title="All Series",The 100 S03 E12
http://fortv.cc:8080/series/n7NX45/216258/186714.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/mu79Iw0oKXqaSCP2qfEbeptSm3a.jpg" group-title="All Series",The 100 S03 E13
http://fortv.cc:8080/series/n7NX45/216258/186715.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E14" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/574S0jyVEi244LIbCDW1vA5O2w2.jpg" group-title="All Series",The 100 S03 E14
http://fortv.cc:8080/series/n7NX45/216258/186716.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E15" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/nipAKX8l7bFgG1AohCs39QiF040.jpg" group-title="All Series",The 100 S03 E15
http://fortv.cc:8080/series/n7NX45/216258/186717.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S03 E16" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/bQ7ayEa7XthcwXA7pttPSKvuI3v.jpg" group-title="All Series",The 100 S03 E16
http://fortv.cc:8080/series/n7NX45/216258/186718.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/wTSxOuEkLCCsPCSTOhe84GYPLPp.jpg" group-title="All Series",The 100 S04 E01
http://fortv.cc:8080/series/n7NX45/216258/186719.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/6S7HePaErvRUSaluljq9tsDyEN6.jpg" group-title="All Series",The 100 S04 E02
http://fortv.cc:8080/series/n7NX45/216258/186720.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/5EaRbbNkY7kjJCmUCSjqRNRGXVN.jpg" group-title="All Series",The 100 S04 E03
http://fortv.cc:8080/series/n7NX45/216258/186721.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/pwM1E2SsvyFUSmh7BmT68dVdhiR.jpg" group-title="All Series",The 100 S04 E04
http://fortv.cc:8080/series/n7NX45/216258/186722.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ljl7hd4RuicnfrNGhUo8lAtBH4b.jpg" group-title="All Series",The 100 S04 E05
http://fortv.cc:8080/series/n7NX45/216258/186723.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/v131MISmWphOckgxKqDHuEMAHK6.jpg" group-title="All Series",The 100 S04 E06
http://fortv.cc:8080/series/n7NX45/216258/186724.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/7OVuhckKovYACB4UqTcC9vwmmAl.jpg" group-title="All Series",The 100 S04 E07
http://fortv.cc:8080/series/n7NX45/216258/186725.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/eLvFhMLKcOuWFzDwGeIXU5b7sDH.jpg" group-title="All Series",The 100 S04 E08
http://fortv.cc:8080/series/n7NX45/216258/186726.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/oMmqZKoC6GTDQFTI1u2rBgEfeCL.jpg" group-title="All Series",The 100 S04 E09
http://fortv.cc:8080/series/n7NX45/216258/186727.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/hvXDwX9gbqC1rXSsr3LcSVDIaIN.jpg" group-title="All Series",The 100 S04 E10
http://fortv.cc:8080/series/n7NX45/216258/186728.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/9sYlQPfDiszPjjSllll5qtKcY4H.jpg" group-title="All Series",The 100 S04 E11
http://fortv.cc:8080/series/n7NX45/216258/186729.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/fAgQ0XBGRunNCJVO9uv0QNXhFLx.jpg" group-title="All Series",The 100 S04 E12
http://fortv.cc:8080/series/n7NX45/216258/186730.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S04 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/6eZMGcdGFD4P0c1vXidTOoNwrrt.jpg" group-title="All Series",The 100 S04 E13
http://fortv.cc:8080/series/n7NX45/216258/186731.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/Ahst3NzymbNKYTwshDDyrMiEjKW.jpg" group-title="All Series",The 100 S05 E01
http://fortv.cc:8080/series/n7NX45/216258/186732.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/2zSkahpr2DKiXeZAopFSZDsGt50.jpg" group-title="All Series",The 100 S05 E02
http://fortv.cc:8080/series/n7NX45/216258/186733.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/aBvOleQMesFd7XYLC6Bj3rnYmmG.jpg" group-title="All Series",The 100 S05 E03
http://fortv.cc:8080/series/n7NX45/216258/186734.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/68x5ebjUNyWkPRrM6NWYtsdL4rl.jpg" group-title="All Series",The 100 S05 E04
http://fortv.cc:8080/series/n7NX45/216258/186735.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/vnL9EBCBq5l37qzHYhNUdyBkxUA.jpg" group-title="All Series",The 100 S05 E05
http://fortv.cc:8080/series/n7NX45/216258/186736.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/fhz3Fq7mkP37Yb1MeF9inKigq0R.jpg" group-title="All Series",The 100 S05 E06
http://fortv.cc:8080/series/n7NX45/216258/186737.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/7M85pUFfGK4D68hnsNR9HjAA8pt.jpg" group-title="All Series",The 100 S05 E07
http://fortv.cc:8080/series/n7NX45/216258/186738.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ib60yXJAMOn2zlAIPFRyPVNDGop.jpg" group-title="All Series",The 100 S05 E08
http://fortv.cc:8080/series/n7NX45/216258/186739.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/yUPUVgNzVGnYhZkDPdGNEyB7Jcj.jpg" group-title="All Series",The 100 S05 E09
http://fortv.cc:8080/series/n7NX45/216258/186740.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/uc8Tbtha9vHZreKsOLtlsd2eZve.jpg" group-title="All Series",The 100 S05 E10
http://fortv.cc:8080/series/n7NX45/216258/186741.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/hmYvmwSajYG4c4qjl00Lq3ULJo5.jpg" group-title="All Series",The 100 S05 E11
http://fortv.cc:8080/series/n7NX45/216258/186742.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/pDa9pNpMkTWBj1QfObo3BECj4J8.jpg" group-title="All Series",The 100 S05 E12
http://fortv.cc:8080/series/n7NX45/216258/186743.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S05 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/J4FtYgQpMMbvgri0klysNo9jM7.jpg" group-title="All Series",The 100 S05 E13
http://fortv.cc:8080/series/n7NX45/216258/186744.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/rlMqEawRiHQPVdaCGNKcnk59WNt.jpg" group-title="All Series",The 100 S06 E01
http://fortv.cc:8080/series/n7NX45/216258/186745.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/yJKTDjnWn6tDFI32ss3DZoNJdE1.jpg" group-title="All Series",The 100 S06 E02
http://fortv.cc:8080/series/n7NX45/216258/186746.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/qrk8TdSEXg6jlwcw60e93qH0M7R.jpg" group-title="All Series",The 100 S06 E03
http://fortv.cc:8080/series/n7NX45/216258/186747.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/wzF7lUcYRJySgsURQr0bhWibcu6.jpg" group-title="All Series",The 100 S06 E04
http://fortv.cc:8080/series/n7NX45/216258/186748.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/vIZPo7EZePdoYtUE09msXGEkZr6.jpg" group-title="All Series",The 100 S06 E05
http://fortv.cc:8080/series/n7NX45/216258/186749.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/3ndZzRY19pYS5XeTFS1KF33S9KP.jpg" group-title="All Series",The 100 S06 E06
http://fortv.cc:8080/series/n7NX45/216258/186750.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/kkmvYqXQA4zDBFsstzX1BntQnsZ.jpg" group-title="All Series",The 100 S06 E07
http://fortv.cc:8080/series/n7NX45/216258/186751.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/qP9jVlVWI1rXLjZmhYqDuCFREEy.jpg" group-title="All Series",The 100 S06 E08
http://fortv.cc:8080/series/n7NX45/216258/186752.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/ckYny8nadEeYkTfsEm5oLXbSnOJ.jpg" group-title="All Series",The 100 S06 E09
http://fortv.cc:8080/series/n7NX45/216258/186753.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/g5znG4J9D66qq5lfNzqCglug184.jpg" group-title="All Series",The 100 S06 E10
http://fortv.cc:8080/series/n7NX45/216258/186754.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/efYEcVpBOkoJVQis3d2ViJQqFHW.jpg" group-title="All Series",The 100 S06 E11
http://fortv.cc:8080/series/n7NX45/216258/186755.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/5MqBYIoVKgiSXAQy82AET8PDfoq.jpg" group-title="All Series",The 100 S06 E12
http://fortv.cc:8080/series/n7NX45/216258/186756.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S06 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/eCOBBsR7SXNjRGg4qAgucwHEYEk.jpg" group-title="All Series",The 100 S06 E13
http://fortv.cc:8080/series/n7NX45/216258/186757.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E01" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/oBxyJWUCqrZ9kjcK2yzzRsjehLH.jpg" group-title="All Series",The 100 S07 E01
http://fortv.cc:8080/series/n7NX45/216258/186758.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E02" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/4vIJORH8PE19GIkkw4vUPrCb2Cc.jpg" group-title="All Series",The 100 S07 E02
http://fortv.cc:8080/series/n7NX45/216258/186759.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E03" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/gZGyhRTAHSPn3FjBWzMqMFsMeFe.jpg" group-title="All Series",The 100 S07 E03
http://fortv.cc:8080/series/n7NX45/216258/186760.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E04" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/1pXGLPRv9MwLZQ7Utle7TJMTHa1.jpg" group-title="All Series",The 100 S07 E04
http://fortv.cc:8080/series/n7NX45/216258/186761.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E05" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/qr1hu3MmpUCPZdbhinMDstZ1Xvx.jpg" group-title="All Series",The 100 S07 E05
http://fortv.cc:8080/series/n7NX45/216258/186762.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E06" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/wN2jKNIZrDAADXdj6dfF4ert8yh.jpg" group-title="All Series",The 100 S07 E06
http://fortv.cc:8080/series/n7NX45/216258/186763.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E07" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/5CY79ewUpcmK0FewSbv46c8V41M.jpg" group-title="All Series",The 100 S07 E07
http://fortv.cc:8080/series/n7NX45/216258/186764.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E08" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/fZj6iUHQhd1YgCDvhcRdCcVySLJ.jpg" group-title="All Series",The 100 S07 E08
http://fortv.cc:8080/series/n7NX45/216258/186765.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E09" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/xZUAhZlj9BOIeFo2soDRIWoLcGf.jpg" group-title="All Series",The 100 S07 E09
http://fortv.cc:8080/series/n7NX45/216258/186766.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E10" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/kvgpGFaDEJMk05BXRZ4MpXEa80a.jpg" group-title="All Series",The 100 S07 E10
http://fortv.cc:8080/series/n7NX45/216258/186767.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E11" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/h1AZ4xfLMtqSF7ULCPOaOyyGDPD.jpg" group-title="All Series",The 100 S07 E11
http://fortv.cc:8080/series/n7NX45/216258/186768.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E12" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/hsVZkqirhrw3T0jFvyDuxF9mrw1.jpg" group-title="All Series",The 100 S07 E12
http://fortv.cc:8080/series/n7NX45/216258/186769.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E13" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/r61WmOBHnwLWyuX61HvTOKsRChl.jpg" group-title="All Series",The 100 S07 E13
http://fortv.cc:8080/series/n7NX45/216258/186770.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E14" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/bcImqW5fBFCJkAHQmyO0sy8Z6Ix.jpg" group-title="All Series",The 100 S07 E14
http://fortv.cc:8080/series/n7NX45/216258/186771.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E15" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/fzRtic9p1FVJsFdJ4M8LSYzNKcN.jpg" group-title="All Series",The 100 S07 E15
http://fortv.cc:8080/series/n7NX45/216258/186772.mkv
#EXTINF:-1 tvg-id="" tvg-name="The 100 S07 E16" tvg-logo="https://image.tmdb.org/t/p/w600_and_h900_bestv2/zUZTFrSu7OSq53FVBm99wolZFSa.jpg" group-title="All Series",The 100 S07 E16
http://fortv.cc:8080/series/n7NX45/216258/186773.mkv

"""

lines = full_input_text_extended.strip().splitlines()

result = []
for i in range(0, len(lines), 2):
    if i + 1 < len(lines):
        title_line = lines[i]
        link_line = lines[i + 1].strip()

        match = re.search(r'tvg-name="([^"]+)"', title_line)
        if match:
            base_name = match.group(1).strip()
            ext = os.path.splitext(link_line)[1]
            full_filename = base_name + ext

            # Extract Sxx and Exx if available
            season_match = re.search(r'[Ss](\d{1,2})', base_name)
            episode_match = re.search(r'[Ee](\d{1,2})', base_name)

            season = f"S{int(season_match.group(1)):02}" if season_match else ""
            episode = f"E{int(episode_match.group(1)):02}" if episode_match else ""

            result.append((base_name, full_filename, link_line, season, episode))

# Create DataFrame
df = pd.DataFrame(result, columns=[
    "File Name", 
    "Full File Name", 
    "Download Link", 
    "Season", 
    "Episode"
])

# Save to CSV
df.to_csv("MillionDollarListing.csv", index=False)
print("✅ Saved as output_with_season_episode.csv")
