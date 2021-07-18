from functools import reduce
import discord
from discord import client
from discord import colour
from discord import embeds
from discord.ext import commands
import os
  

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
     print('다음으로 로그인합니다: ')
     print(client.user.name)
     print('connection was succesful')

     # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
     await client.change_presence(status=discord.Status.online)

     await client.change_presence(activity=discord.Game(name="게임 하는중"))
     #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
     #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
     #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
     print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event
async def on_message(message):
        if message.content.startswith("!공명"):
            await message.channel.send("주공, (!교지)로 명령을.")

        if message.content.startswith("!이지"):
            await message.channel.send("https://www.inven.co.kr/board/lol/3372/480627")
        
        if message.content.startswith("""!노래"""):
               await message.channel.send("""플레이리스트

!p sequance 아이즈원
!p not shy
!p bang!
!p christopher - bad
!p Johnny Stimson - Gimme Gimme
!p crazy over you
!p wannabe
!p mad circuit - my fit
!p why dont we rain
!p weki meki cool
!p khalid - talk
!p un village
!p pretty savage
!p 브레이브걸스 We Ride
!p 아이즈원) AYAYAYA
!p 있지 Sorry Not Sorry
!p BAEKHYUN Bambi
!P RED VELVET RBB
!P 놀이 Naughty
!P 아이즈원 Mise-en-Scène
!P  레드벨벳 빨간 맛
!P 레드벨벳 Bad Boy
!P 레드벨벳 Rookie
!P 레드벨벳 피카부
!P 레드벨벳 Dumb Dumb
!P 트와이스 Alcohol-Free
!P I Can't Stop Me
!P More & More
!P Feel Special
!P Cry For Me""")

        if message.content.startswith("""!교지"""):
            await message.channel.send("""
주공, 이번의 명령 선택지는 다음과 같습니다.

!공명 - 작동 테스트
!인사 - 공명의 인삿말
!이지 - 롤 이모티콘 모음 링크
!출사표 - 전출사표 원문
!노래 - 노래 모음
!짜오공략 - 각종 짜오 공략 커맨드
!패 - 미리 써둔 장문의 패드립 모음 
!무한~ - 무야호
!삼국 - 삼탈워 공략글
!투표 - !투표 "투표주제" 
!짤 - 각종 짤 명령어
!개발 - 개발과정""")

        if message.content.startswith("""!짜오공략"""):
            await message.channel.send("""
주공, 호위장군 조운이 당도하였나이다
            
!짜오룬 - 짜오의 룬과 주의사항
!짜오템 - 짜오의 템과 연구사항
!짜오팁 - 동선 및 자잘한 팁""")

        if message.content.startswith("""!짜오룬"""):
            await message.channel.send("""
빛망 너프 먹은 시점에서, 보조룬은 무조건 마법/지배로 고정
상성 극복엔 결의- 뼈방패 생명샘 (렉사이, 뽀삐, 워윅, 트런들)
정복자 - 내가 딜을 내고 안정적인 앞라인, 상대 탱커 다수 (단점을 모르겠다. 최고)
칼날비 - 빠른 갱과 빠른 콤보, 상대 물몸 다수 (유통기한이 제일 빠름)
난입 - 상대 정글(킨드 니달리 릴리아 등)이 기동성이 좋으면 1ㄷ1 우세, 빠른 갱 가능 (킬 좀 먹어야됨)
룬을 고정한다면 플레이에는 변함이 없겠지만 변하는 상황에 유동적으로 대응 불가 
신짜오의 한계를 본인이 극대화하는 꼴이므로 룬은 항상 유동적으로..""")

        if message.content.startswith("!짜오템"):
            await message.channel.send(""" 
월식 - 국룰템, 그냥 무난하고 선혈 올리기 싫을때 올리는거. 성능은 확실함
정수 - 스킬가속, 마나, 극딜 짜오에게는 필수적이지만 팀에 탱커 적으면 고민해볼것
선혈 - 고티어들의 선택, 피흡과 안정적인 앞라인 가능. 허나 쓰는 템이라 적응과 인지 필요
몰왕 - (이젠 놔주자) w가 너프 먹으면서 월식 2티어에서 밀려난 템. 초반 진짜 잘 컸으면 가도 될듯
철갑궁 - (평상엔 효율 별로) 내가 시발 역대급으로 잘컸다 싶으면 한번 쯤 가볼 만한 템
치감 관련 - 가갑 : 내가 쳐맞는다, 내가 때린다 -치감칼
스테락 - 팀에 탱커 없거나 안정적인 딜링이 필요할때. 난 개인적으론 불호 (이거가면 장점이 안나옴)
마최, 주문포식자, 헤르메스 - 상대 ap 다수 (3~5)
발분 - 예전엔 나름 쓸만했는데 지금은 하두 너프때려서 모르겠음
가엔 - 위에서 한 2-3개 올리면 무조건 가는 템 
죽무 - 나름 갈만한거 같으면서도,,딴거가는게 더 좋은듯한 계륵템
토마호크, 닌탑 - 상대 ad 다수 (3~5)
쿨감신, 공속신 - 내가 스킬가속이 부족하다 & 내가 콤보를 빨리 넣어야 한다""")
         
        if message.content.startswith("!패"):
            await message.channel.send("""주공, 공명의 이 세치 혀를 감히 놀려보겠습니다.
이 중에 하나를 골라 주시옵서서. (!ㅍ1) (!ㅍ2) (!ㅍ3)""")

        if message.content.startswith("""!ㅍ1"""):
            await message.channel.send("""ㅋㅋ 유미없는놈 니 할ㅁ 유골함 뽀개서 물고기 밥으로 주기 전에 니네 할ㅂ jot마냥 다물어라 입 ㅋ""")

        if message.content.startswith("""!ㅍ2"""):
            await message.channel.send("""
ni aemy가 전두엽 갈려버린 상태에서 애낳았누,,? 패드립 맛보고도 옆집 병태 할아버지가 주는 미약 중독된 니 할매마냥
못참고 ㅋ.ㅋ 좋은말로 타일러서 보내려고 했는뎅..왜 인걸 왜 못믿어 친구야~시팅 받았으면 곱게 원숭이마냥
' 감사합니다 주인님 ㅠㅠ' 할 것이지,,형은 너처럼 에서 부들거리지 않아요~왜 지애bl마냥 노잼이네 ㅋ""") 

        if message.content.startswith("""!ㅍ3"""):
            await message.channel.send("""
너도 참 불쌍해 어찌보면? 니 부모 유전자 받고 자라서 얼굴 모르는 ㅅ끼한테 욕도 시원하게 한사발 받고? 니 할미 유골통 까버리기 전에 그만해야지 ㅋㅋ 
니네 부모는 니 조부모 모실 돈도 없어서 무덤 하나 못해주니까 산에 버리고 와서 까마귀밥 컷! 해버리는데 왜...그 꼴 보고도 사릴줄을 몰라? 형은 니 엄마 메차쿠ㅊ 범하러 간다 ㅋ""")

        if message.content.startswith("!투표"):
           vote = message.content[4:].split(" / ")
           channel = message.channel
           await channel.send("투표를 시작하겠습니다.")
           for i in range(0, len(vote)):
               lastsend = await channel.send("```" + vote[i] + "```")
               await lastsend.add_reaction('👍')
               await lastsend.add_reaction('👎')
        
        if message.content.startswith("""!삼국"""):
            await message.channel.send("""
        주공, 한실부흥을 위해 전력을 다하겠나이다.
!조조 (https://namu.wiki/w/%ED%86%A0%ED%83%88%20%EC%9B%8C:%20%EC%82%BC%EA%B5%AD/%EC%84%B8%EB%A0%A5/%EC%A1%B0%EC%A1%B0)
!유비 (https://namu.wiki/w/%ED%86%A0%ED%83%88%20%EC%9B%8C:%20%EC%82%BC%EA%B5%AD/%EC%84%B8%EB%A0%A5/%EC%9C%A0%EB%B9%84)
!손오  (https://namu.wiki/w/%ED%86%A0%ED%83%88%20%EC%9B%8C:%20%EC%82%BC%EA%B5%AD/%EC%84%B8%EB%A0%A5/%EC%86%90%EA%B2%AC)
!원소  (https://namu.wiki/w/%ED%86%A0%ED%83%88%20%EC%9B%8C:%20%EC%82%BC%EA%B5%AD/%EC%84%B8%EB%A0%A5/%EC%9B%90%EC%86%8C)
!공손찬 (https://namu.wiki/w/%ED%86%A0%ED%83%88%20%EC%9B%8C:%20%EC%82%BC%EA%B5%AD/%EC%84%B8%EB%A0%A5/%EA%B3%B5%EC%86%90%EC%B0%AC) `);""")
        
        if message.content.startswith("""!짤"""):
            await message.channel.send("""
!cut(한글로) - 바디 파괴 짤
!shup - 닥쳐!
!무부 - 무군무부의 말이로다
!ㅋㅋ 이는 천하의 웃음거리요
!자 - 드가자~
!관짝 - 통곡짤 
!ㅂㅂ - ㅂㅂ""")
   
        if message.content.startswith("!인사"): 
         embed=discord.Embed(title="융중의 공명이 기나긴 기다림 끝에 초려에서 나왔습니다. 과거의 관중과 장량처럼 여러분을 보좌할 것이며, 멈추지 않고 죽어서 멈추겠나이다")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMzMg/MDAxNjI2NjMzMTcxNDI1.5FQQ_Rdn8tDY4YA8CQ55WsUdjeiWVaRSvRhifx1ZhNgg.V7vh2izVjUiikf1qH_hTThKHnKykEwQhjQd2umK9wp8g.JPEG.zaang030514/20210719_032222.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!무한~"): 
         embed=discord.Embed(title="무~야호~")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://media.vlpt.us/images/composite/post/d575d7e7-f7ef-4db3-b55b-1dbd9b249567/img.png")
         await message.channel.send(embed=embed)

        if message.content.startswith("!컷"): 
         embed=discord.Embed(title="vardy`s on fire🔥")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMTMy/MDAxNjI2NjM0OTY2Njgw.H8CJaw5hUATWF_GL-bc3DBdyIqMw2KOl3LmC7Abdjkog.RiZuI-3wyGsDNNErGrLqPQkDPJGkSbyltdPQapsW53sg.JPEG.zaang030514/FB_IMG_1626631781942.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!ㅂㅂ"): 
         embed=discord.Embed(title="再见!")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMTkx/MDAxNjI2NjM0OTY2NjY2.kXQjRjywiXVyPY72e13C-IoiL3fO_BLZ5yAUrChZ2CQg.rIep6AQ9pmd6hZ9jqQRmQ70gL1Bk-a_3d72cgpM7sxwg.JPEG.zaang030514/1626634851471-8.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!관짝"): 
         embed=discord.Embed(title="")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMTQ0/MDAxNjI2NjM0OTY2NTQy.cNXRKwsFL_zwnKPWBHPKRTOFu8DZpKXxSdIEwliXPqsg.KrToTcxwnTR9QzJjGTpvpFNxKToeyZQmCeRvlDknn84g.JPEG.zaang030514/1626634851471-6.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!자"): 
         embed=discord.Embed(title="드가자~")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMjU1/MDAxNjI2NjM0OTY2MjA3.nMcWZkHgFjyJtxCvkqGfL4YyrrfTy6JH4OXOSnumT7gg.ubWYts2-xxmyHOEK_T_rcFMoFw0eqlIjBl6ezn8IHR0g.JPEG.zaang030514/1626634851471-5.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!ㅋㅋ"): 
         embed=discord.Embed(title="")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMTk0/MDAxNjI2NjM0OTY2MjUz.xQj_sr-jTNQq5veVQoQZZ-n6P3V04d-9_FQ9WFpDINYg.HSdljYu6nQ615A0C5Xhj-5GvKT5tci-ZEag-lxyujlog.JPEG.zaang030514/1626634851471-1.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!무부"): 
         embed=discord.Embed(title="")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMjAw/MDAxNjI2NjM0OTY2MjY5.PEo5YtR3edaj_8z4dghBHhBE8hgy-OcI4jhj6MeehYIg.Gq-ZLBZotshOiQ6cDa_snKTpgIDVf6vBQ8EnxF_37zUg.JPEG.zaang030514/1626634851471-0.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!shup"): 
         embed=discord.Embed(title="")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMTE5/MDAxNjI2NjM0OTY2MjY0.NOT2ioWddM6089_ll98Z2AqPuJ9qRBKxsTMJWqw4G9kg.k6ui-gJrzgf84VO8aLZ5DWW_Wyx31Z79SIVnCGvYRVAg.JPEG.zaang030514/1626634851471-4.jpg?type=w773")
         await message.channel.send(embed=embed)
        
        if message.content.startswith("""!개발"""): 
         embed=discord.Embed(title="""량, 어찌 주공의 은혜를 갚으리오.
         
2021.07.17 node.js 디스코드 봇 생성 및 !공명 명령어 입력
2021.07.18 봇 호스팅 시도..실패 후 파이썬으로 체제 변경
2021.07.19 node 파이썬 변환 성공 및 명령어 추가 입력""")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfNjMg/MDAxNjI2NjM3Nzc1OTA0.yubQ5zl5mnLO61_zGLt0kTYd4VlbSC7hIalu5Xetf58g.BhRenjPXfmjXaT9N3jk5mW7D1umOu9n2L-zvdmo8jMYg.JPEG.zaang030514/9b16bc74b72947d18f45be8a3c5c3922.jpg?type=w773")
         await message.channel.send(embed=embed)

        if message.content.startswith("!24"): 
         embed=discord.Embed(title="드디어 공명봇이 24시간 호스팅 성공했습니다!")
         embed.set_thumbnail(url="")
         embed.set_image(url="https://postfiles.pstatic.net/MjAyMTA3MTlfMjc5/MDAxNjI2NjM0OTY2NTUx.A-SfgRrsqgsS1m1Snq8GYLsah_NpAfEyGP2o0S9WMK4g.LmRmAoMz5OnnRHj1_8_O2rpSgnMWn9c0nJdN4FEL1zkg.JPEG.zaang030514/1626634851471-7.jpg?type=w773")
         await message.channel.send(embed=embed)


client.run(os.environ['token'])