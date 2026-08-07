# -*- coding: utf-8 -*-
"""Long-form content for the Journal and the Expansion projects.

Editorial rules held throughout:
  · No invented statistics. Where a number would be persuasive but is not
    verified, the sentence is rewritten to work without it.
  · No project is described as finished. No revenue, signed leases, store
    counts, investment amounts or completed government agreements.
  · No client is named.
  · Anything that touches law, tax, immigration, licensing or real estate
    carries an advisory note pointing to qualified U.S. professionals.
  · Chinese is written for a Taiwanese owner, not translated from English.
"""

CTA = 'https://www.surveycake.com/s/3qKZN'

# ── shared interface strings ────────────────────────────────────────────────
UI = {
    'en': dict(
        skip='Skip to content', navLabel='Primary', navLabelMobile='Mobile',
        langLabel='Language', open='Open menu', close='Close menu',
        cta='Start Your Expansion', ctaLong='Book a Strategy Session',
        home='Home', journal='The Expansion Journal', projects='Expansion in Progress',
        breadcrumb='Breadcrumb',
        catLabel='Category', readLabel='Reading time', updatedLabel='Updated',
        statusLabel='Status', industryLabel='Industry',
        back='Back to The Expansion Journal', backProjects='Back to Expansion in Progress',
        related='Related reading', relatedNote='More from CnC Venture',
        infoLabel='Project information',
        docCtaHead='Ready to Explore the U.S. Market?',
        docCtaBody='Start with a focused conversation about your company, your expansion '
                   'goals and the markets you are weighing up. We will help you identify the '
                   'most practical next step.',
        docCtaBtn='Start Your Expansion Assessment',
        ctaLabel='Book a strategy session',
        ctaHead='Ready to Build Your Next Chapter?',
        ctaBody='Start with a focused conversation about your company, expansion goals, '
                'timeline, and the U.S. market opportunities you are considering. We will '
                'help you identify the most practical next step.',
        ctaImgAlt='Golden light across a saguaro hillside in Arizona',
        tagline='Expand Beyond Borders.',
        copyright='© 2026 CnC Venture. A business expansion platform.',
        route='Taiwan → United States',
        # ── listing pages and article navigation ──────────────────────
        allLabel='All',
        prevLabel='Previous', nextLabel='Next', pagerLabel='Article navigation',
        emptyCategory='Nothing has been published in this section yet. '
                      'New pieces appear here as they are written.',
        journalDesc='A business magazine on building in America — market reports, city '
                    'guides, expansion stories and the considerations behind each decision.',
        journalStand='Market overviews, city guides and practical playbooks for companies '
                     'building a presence in the United States.',
        journalHeroAlt='Red rock country near Sedona, Arizona',
        projectsDesc='Live engagements, reported as they stand. These are ongoing '
                     'projects, not finished case studies.',
        projectsStand='Live engagements, reported as they stand. We will publish outcomes '
                      'when there are outcomes to publish.',
        projectsHeroAlt='Office towers in downtown Phoenix',
        nav=[('About', '/{s}/about/'), ('Services', '/{s}/services/'),
             ('Industries', '/{s}/#industries'), ('Expansion Stories', '/{s}/#stories'),
             ('Insights', '/{s}/#insights'), ('Arizona', '/{s}/#arizona'),
             ('Contact', '/{s}/contact/')],
        footer=[('Platform', [('About', '/{s}/about/'), ('Services', '/{s}/services/'),
                              ('Expansion Journey', '/{s}/#journey'),
                              ('Industries', '/{s}/#industries'),
                              ('Partner Ecosystem', '/{s}/#partners')]),
                ('Journal', [('Insights', '/{s}/#insights'),
                             ('Arizona City Guide', '/{s}/#cities'),
                             ('Expansion in Progress', '/{s}/#stories'),
                             ('Why Arizona', '/{s}/#arizona')]),
                ('Contact', [('Book a strategy session', CTA), ('Contact', '/{s}/contact/'),
                             ('Phoenix, Arizona', None), ('Taipei, Taiwan', None)])],
    ),
    'zh-tw': dict(
        skip='跳至主要內容', navLabel='主要導覽', navLabelMobile='行動版導覽',
        langLabel='語言', open='開啟選單', close='關閉選單',
        cta='開始美國拓展評估', ctaLong='預約策略諮詢',
        home='首頁', journal='拓展誌', projects='進行中的專案',
        breadcrumb='麵包屑導覽',
        catLabel='分類', readLabel='閱讀時間', updatedLabel='更新',
        statusLabel='狀態', industryLabel='產業',
        back='返回拓展觀點', backProjects='返回進行中的專案',
        related='延伸閱讀', relatedNote='更多來自 CnC Venture',
        infoLabel='專案資訊',
        docCtaHead='準備好探索美國市場了嗎？',
        docCtaBody='先從一場聚焦的對話開始——談你的公司、拓展目標，以及你正在權衡的市場。'
                   '我們會協助你找出最務實的下一步。',
        docCtaBtn='開始美國拓展評估',
        ctaLabel='預約策略諮詢',
        ctaHead='準備好，寫下你的下一章了嗎？',
        ctaBody='先從一場聚焦的對話開始——談你的公司、拓展目標、時程，以及你正在評估的'
                '美國市場機會。我們會協助你找出最務實的下一步。',
        ctaImgAlt='金色光線灑落亞利桑那的巨柱仙人掌山坡',
        tagline='讓世界，看見你的下一步。',
        copyright='© 2026 CnC Venture. 企業海外拓展平台。',
        route='台灣 → 美國',
        # ── 列表頁與文章導覽 ──────────────────────────────────────────
        allLabel='全部',
        prevLabel='上一篇', nextLabel='下一篇', pagerLabel='文章導覽',
        emptyCategory='這個分類還沒有文章。新的內容寫好之後，會出現在這裡。',
        journalDesc='一本關於「在美國落地」的商業誌——市場觀察、城市指南、創業案例，'
                    '以及每個決定背後的真實考量。',
        journalStand='給正在美國建立據點的企業：市場觀察、城市指南與實務指引。',
        journalHeroAlt='亞利桑那州 Sedona 一帶的紅岩地景',
        projectsDesc='進行中的合作，如實呈現。這些是正在進行的專案，不是完成的案例。',
        projectsStand='進行中的合作，如實呈現。有成果的時候，我們再談成果。',
        projectsHeroAlt='Phoenix 市中心的辦公大樓',
        nav=[('關於', '/{s}/about/'), ('服務', '/{s}/services/'),
             ('產業', '/{s}/#industries'), ('專案', '/{s}/#stories'),
             ('觀點', '/{s}/#insights'), ('亞利桑那', '/{s}/#arizona'),
             ('聯絡', '/{s}/contact/')],
        footer=[('平台', [('關於', '/{s}/about/'), ('服務', '/{s}/services/'),
                          ('拓展歷程', '/{s}/#journey'), ('產業', '/{s}/#industries'),
                          ('合作生態系', '/{s}/#partners')]),
                ('拓展誌', [('觀點', '/{s}/#insights'),
                            ('亞利桑那城市指南', '/{s}/#cities'),
                            ('進行中的專案', '/{s}/#stories'),
                            ('為什麼是亞利桑那', '/{s}/#arizona')]),
                ('聯絡', [('預約策略諮詢', CTA), ('聯絡我們', '/{s}/contact/'),
                          ('Phoenix, Arizona', None), ('台北，台灣', None)])],
    ),
}

ADV_EN = ('Requirements differ by city, county, property and business type, and they '
          'change. Treat everything here as orientation, not advice — confirm the '
          'specifics with qualified U.S. legal, accounting, tax, immigration, '
          'real-estate and licensing professionals before you commit.')
ADV_ZH = ('相關規定會因城市、郡、物件與業態而不同，也會隨時間調整。這裡的內容是幫助你建立方向感，'
          '不是專業建議——實際做決定前，請與具備資格的美國律師、會計師、稅務、移民、不動產與'
          '證照顧問確認細節。')

PAGES = {}

# ═══════════════════════════════════════════════════════════════════════════
# ARTICLE 01
# ═══════════════════════════════════════════════════════════════════════════
PAGES['arizona-gateway-for-taiwanese-companies'] = {
    'type': 'article', 'hero': 'hero-gateway.jpg',
    'related': ['phoenix-metro-market-guide', 'taiwan-startup-delegation-arizona'],
    'en': dict(
        category='Market Overview', readingTime='9 min read',
        published='2026-08-06', updated='2026-08-06', dateLabel='August 2026',
        crumb='Arizona as a strategic gateway',
        title='Why Arizona Is Becoming a Strategic Gateway for Taiwanese Companies',
        desc='An introduction to Arizona\'s business ecosystem, major industries, '
             'Taiwanese connections, and what companies should evaluate before entering '
             'the U.S. market through Greater Phoenix.',
        heroAlt='Greater Phoenix at dusk, seen from the surrounding mountains',
        cardBlurb='What the ecosystem actually offers, and what to evaluate before deciding.',
        standfirst='Arizona has moved from the margin of the American map to the middle of '
                   'a conversation about where things get built. For companies arriving from '
                   'Taiwan, the question is not whether the state is growing — it is whether '
                   'its particular kind of growth fits what you are trying to do.',
        body=[
            ('h2', 'Why Arizona is receiving attention'),
            ('p', 'For most of the past three decades, a Taiwanese company entering the United '
                  'States looked first at California, then at Texas. Arizona was a place you '
                  'flew over. That has changed, and it has changed for a reason that is '
                  'structural rather than promotional: a concentration of advanced '
                  'manufacturing investment has arrived in the state, and a supply chain has '
                  'started to follow it.'),
            ('p', 'What makes this relevant to a Taiwanese business is not the headline '
                  'projects themselves. It is the second and third order effects — the '
                  'suppliers, the service firms, the contractors, the logistics operators and '
                  'the workforce that assemble around large industrial commitments. That '
                  'ecosystem is being built now, which means there is still room in it.'),
            ('h2', 'The semiconductor and advanced-manufacturing ecosystem'),
            ('p', 'Arizona\'s advanced-manufacturing base is anchored by large-scale '
                  'semiconductor investment in the Phoenix metropolitan area, with Chandler '
                  'and north Phoenix as the two most visible centres of gravity. Around those '
                  'anchors sit the categories that a fab actually consumes: specialty '
                  'chemicals and gases, precision components, tooling, calibration and '
                  'metrology services, cleanroom construction, industrial gases, waste '
                  'handling, and the freight and warehousing that move all of it.'),
            ('p', 'If your company already supplies any part of that chain in Taiwan, the '
                  'strategic question is straightforward: do your customers expect a U.S. '
                  'presence, and if so, on what timeline? That question is usually more '
                  'useful than any general assessment of the state.'),
            ('pull', 'A fab is not a building. It is a demand signal — and the companies that '
                     'answer it early are the ones with room to negotiate.', None),
            ('h2', 'Connections with Taiwanese companies and suppliers'),
            ('p', 'One of the practical advantages of Arizona for a Taiwanese company is that '
                  'you will not be the first. A Mandarin-speaking business community has been '
                  'forming in the metro area alongside the manufacturing investment: '
                  'suppliers who have already been through U.S. qualification, professionals '
                  'who have handled cross-border entity structures, and operators who have '
                  'made the same mistakes you are about to consider making.'),
            ('p', 'This matters more than it sounds. The cost of entering a market is largely '
                  'the cost of learning it, and that cost falls sharply when there are people '
                  'nearby who will tell you honestly what a thing should cost and how long it '
                  'should take.'),
            ('fig', 'city-phoenix.jpg', 'Downtown Phoenix',
             'Downtown Phoenix. Beyond the manufacturing story, Greater Phoenix is a '
             'metropolitan market in its own right.'),
            ('h2', 'Greater Phoenix as a business market'),
            ('p', 'Beyond manufacturing, Greater Phoenix is a large and still-growing '
                  'metropolitan market in its own right — one of the major population centres '
                  'of the western United States, with a consumer base, a services economy and '
                  'a construction sector that operate independently of the semiconductor '
                  'story.'),
            ('p', 'For a restaurant group, a consumer brand or a retail concept, that is the '
                  'more relevant frame. You are not entering a technology corridor. You are '
                  'entering a metro area of several million people with distinct '
                  'sub-markets, and the choice of which sub-market matters a great deal. '
                  'That is the subject of a separate guide.'),
            ('h2', 'Government and economic-development resources'),
            ('p', 'Arizona has an active economic-development apparatus at both state and '
                  'city level. In practice this means there are teams whose job is to help '
                  'companies understand local requirements, connect them with municipal '
                  'departments, and explain what programmes exist. They are a genuine '
                  'resource and they are usually willing to meet.'),
            ('p', 'What they are not is a shortcut. No economic-development office decides '
                  'permits, guarantees incentives, or accelerates an inspection. Approaching '
                  'them as an information channel is productive; approaching them as leverage '
                  'is not.'),
            ('advisory', ADV_EN),
            ('h2', 'Why Arizona can work as a first U.S. landing point'),
            ('p', 'Three characteristics tend to matter to companies making a first entry. '
                  'Operating costs are generally lower than in the largest coastal metros, '
                  'which changes what a first year can be attempted on. Land and industrial '
                  'space have historically been more available, which matters for anyone who '
                  'needs to build rather than lease. And the market is large enough to be a '
                  'real test but not so large that a first mistake is fatal.'),
            ('p', 'The counterweight is that Arizona is not a substitute for California or '
                  'New York if your customers, investors or talent pool are concentrated '
                  'there. A landing point should be chosen against where your business '
                  'actually needs to be, not against where growth is fastest.'),
            ('h2', 'Which companies may be suitable'),
            ('ul', [
                '<strong>Component and materials suppliers</strong> whose customers have '
                'already committed to Arizona capacity.',
                '<strong>Manufacturers and industrial service firms</strong> that need land, '
                'power and space rather than proximity to a coastal port.',
                '<strong>Food and beverage brands</strong> testing a U.S. concept in a market '
                'where build-out and occupancy costs are more forgiving than a coastal debut.',
                '<strong>Consumer and lifestyle brands</strong> looking for a launch market '
                'small enough to learn in and large enough to be meaningful.',
                '<strong>Technology companies and startups</strong> that value proximity to a '
                'university pipeline and a forming ecosystem over a mature one.',
            ]),
            ('h2', 'What companies should evaluate before deciding'),
            ('p', 'The most common failure in market selection is deciding first and '
                  'validating afterwards. A more useful sequence starts with questions that '
                  'have concrete answers.'),
            ('panel', 'Key questions', 'Before you commit to Arizona', [
                'Where are your existing or target U.S. customers, and how much does '
                'proximity actually change the relationship?',
                'What does your business need most — land, labour, talent, logistics, or '
                'consumer density? Rank them.',
                'Which city inside Greater Phoenix serves that need, and have you walked it?',
                'What is the realistic permitting and build-out timeline for your specific '
                'use, in that specific municipality?',
                'Who are the professionals — accountant, attorney, broker — you would rely '
                'on, and have you met them?',
                'What does a conservative first-year budget look like, including the months '
                'before any revenue?',
            ], 'Any question you cannot answer yet is not a reason to stop. It is the next '
               'piece of work.'),
            ('h2', 'How CnC Venture supports the evaluation process'),
            ('p', 'Our role at this stage is not to sell Arizona. It is to help you test it '
                  'against your own business: market research and competitor observation, '
                  'structured site visits across the relevant cities, introductions to '
                  'economic-development teams and to the professional advisors you will need, '
                  'and an honest read on timing.'),
            ('p', 'Some companies finish that process and move. Some finish it and choose a '
                  'different state, or a different year. Both are useful outcomes, and both '
                  'are cheaper than finding out afterwards.'),
        ],
    ),
    'zh-tw': dict(
        category='市場觀察', readingTime='閱讀時間 9 分鐘',
        published='2026-08-06', updated='2026-08-06', dateLabel='2026 年 8 月',
        crumb='亞利桑那作為進入美國的起點',
        title='為什麼亞利桑那正成為台灣企業進入美國的重要起點？',
        desc='從產業結構、重點聚落、台灣連結到大鳳凰城的市場樣貌，帶你理解在選擇這個'
             '落地起點之前，應該先評估哪些事。',
        heroAlt='黃昏時分，自環繞的山區俯瞰大鳳凰城',
        cardBlurb='這個生態系實際提供什麼，以及決定之前該先評估什麼。',
        standfirst='過去三十年，台灣企業進入美國多半先看加州，其次是德州，亞利桑那只是飛越的地方。'
                   '這件事變了。真正該問的不是這個州有沒有在成長，而是它成長的方式，是否符合你想做的事。',
        body=[
            ('h2', '為什麼是現在？'),
            ('p', '亞利桑那近年受到關注，原因是結構性的，不是行銷造出來的：大規模的先進製造投資'
                  '進入了這個州，供應鏈隨之開始移動。'),
            ('p', '對台灣企業真正有意義的，其實不是那些頭條上的大案子，而是它們的第二層與第三層'
                  '效應——圍繞著大型產業投資形成的供應商、專業服務、承包商、物流業者與勞動力。'
                  '這個生態系正在成形中，也就是說，裡面還有位置。'),
            ('h2', '半導體與先進製造聚落'),
            ('p', '亞利桑那的先進製造基礎，集中在大鳳凰城地區的半導體投資，其中 Chandler 與'
                  '北鳳凰城是最明顯的兩個重心。圍繞著這些主體的，是晶圓廠實際會消耗的品項：'
                  '特化與特氣、精密零組件、治具、校驗與量測服務、無塵室工程、工業氣體、廢棄物處理，'
                  '以及承載這一切流動的貨運與倉儲。'),
            ('p', '如果你的公司在台灣已經供應這條鏈上的任何一環，策略問題其實很單純：你的客戶'
                  '是否期待你在美國有據點？如果是，時間點在哪裡？這個問題通常比任何對這個州的'
                  '整體評價都更有用。'),
            ('pull', '一座晶圓廠不只是一棟建築，它是一個需求訊號——而早一步回應的公司，'
                     '是還有談判空間的那一批。', None),
            ('h2', '與台灣企業和供應商的連結'),
            ('p', '亞利桑那對台灣企業的一個實際優勢是：你不會是第一個。隨著製造投資，大鳳凰城'
                  '地區逐漸形成了華語商業社群——已經走過美國供應商認證的同業、處理過跨境公司'
                  '架構的專業人士，以及已經犯過你正打算犯的錯的經營者。'),
            ('p', '這件事比聽起來重要。進入一個市場的成本，很大一部分其實是「學會這個市場」的'
                  '成本；而當附近有人願意誠實告訴你某件事該花多少錢、該花多久，這個成本會大幅下降。'),
            ('fig', 'city-phoenix.jpg', 'Phoenix 市中心',
             'Phoenix 市中心。撇開製造業敘事，大鳳凰城本身就是一個完整的都會市場。'),
            ('h2', '大鳳凰城本身就是一個市場'),
            ('p', '撇開製造業不談，大鳳凰城本身就是一個規模可觀且持續成長的都會市場——美國西部'
                  '主要人口中心之一，擁有自己的消費人口、服務業與營建產業，運作邏輯與半導體'
                  '故事並不相同。'),
            ('p', '對餐飲集團、消費品牌或零售業態而言，這才是更相關的框架。你要進入的不是一條'
                  '科技廊帶，而是一個數百萬人口、內部差異極大的都會區——而選哪一個次市場，'
                  '差別非常大。這是另一篇指南的主題。'),
            ('h2', '政府與經濟發展資源'),
            ('p', '亞利桑那在州與市兩個層級都有積極運作的經濟發展單位。實際上，這代表有一群人的'
                  '工作就是協助企業理解在地規定、對接市政部門、說明有哪些既有計畫可以運用。'
                  '他們是真實可用的資源，通常也願意安排會面。'),
            ('p', '但他們不是捷徑。沒有任何經濟發展辦公室能決定執照、保證優惠或加速查驗。'
                  '把他們當成資訊管道，會很有收穫；把他們當成施壓工具，不會。'),
            ('advisory', ADV_ZH),
            ('h2', '為什麼它可以是第一個落地點'),
            ('p', '對第一次進入美國的企業來說，通常有三件事會發生作用。營運成本普遍低於沿海'
                  '大型都會，這會改變第一年能嘗試的規模；土地與工業空間相對可得，對需要自建'
                  '而非承租的企業特別關鍵；市場規模夠大到能形成真實測試，但又還不至於讓第一個'
                  '錯誤變成致命傷。'),
            ('p', '相對地也要誠實面對：如果你的客戶、投資人或人才都集中在加州或紐約，亞利桑那'
                  '不是它們的替代品。落地點應該對照「你的事業實際需要在哪裡」來選，而不是'
                  '對照「哪裡成長最快」。'),
            ('h2', '哪些企業可能適合'),
            ('ul', [
                '<strong>零組件與材料供應商</strong>——客戶已經確定在亞利桑那布建產能。',
                '<strong>製造業與工業服務業者</strong>——需要的是土地、電力與空間，而非鄰近海港。',
                '<strong>餐飲品牌</strong>——想在裝修與租金相對友善的市場測試美國概念，'
                '而不是直接在沿海城市首發。',
                '<strong>消費與生活品牌</strong>——需要一個小到可以學習、大到有意義的首發市場。',
                '<strong>科技公司與新創</strong>——看重鄰近大學人才管道與成形中的生態系，'
                '而非已經飽和的成熟聚落。',
            ]),
            ('h2', '決定之前，該先評估什麼'),
            ('p', '市場選擇最常見的失敗，是先決定、再驗證。比較有用的順序，是從有具體答案的'
                  '問題開始。'),
            ('panel', '關鍵提問', '在確定亞利桑那之前，先回答這六題', [
                '你現有或目標的美國客戶在哪裡？地理上的接近，實際上會改變多少關係？',
                '你的事業最需要什麼——土地、勞動力、人才、物流，還是消費密度？請排序。',
                '大鳳凰城裡哪一座城市滿足這個需求？你實地走過了嗎？',
                '以你的實際業態、在那個特定市政區，證照與施工的合理時程是多久？',
                '你會倚賴的專業人士——會計師、律師、不動產經紀人——是誰？你見過他們了嗎？',
                '保守估計的第一年預算是什麼樣子？有沒有把還沒有營收的那幾個月算進去？',
            ], '任何一題答不出來，都不是停下來的理由，而是下一件該做的事。'),
            ('h2', 'CnC Venture 在這個階段做什麼'),
            ('p', '我們在這個階段的角色不是推銷亞利桑那，而是協助你用自己的事業去檢驗它：'
                  '市場調研與競爭觀察、跨城市的結構化實地考察、與經濟發展團隊及你日後會需要的'
                  '專業顧問對接，以及對時機的誠實判斷。'),
            ('p', '有些企業走完這個流程就動身；有些走完之後選了別的州，或選了別的年份。'
                  '兩種都是有價值的結果，也都比事後才發現便宜得多。'),
        ],
    ),
}

# ═══════════════════════════════════════════════════════════════════════════
# ARTICLE 02
# ═══════════════════════════════════════════════════════════════════════════
CITIES_EN = [
    ('Phoenix', 'The centre of gravity',
     'State government, the largest employers, the airport and the logistics spine of the '
     'metro. Downtown carries the professional-services and civic weight; the wider city '
     'covers an enormous area with very different conditions inside it.',
     'Professional services, logistics and distribution, headquarters functions, '
     'B2B operations, hospitality serving business travel.',
     'The broadest customer mix in the valley — civic, corporate and residential, across '
     'a wide income range depending on the district.',
     'The deepest inventory of commercial space at the widest range of price points, and '
     'the most established permitting apparatus.',
     'Districts vary enormously. An address five minutes apart can mean a different trade '
     'area, a different customer and a different rent.',
     'Size cuts both ways: it is easy to choose a location that is technically in Phoenix '
     'but functionally in the wrong market.'),
    ('Scottsdale', 'Where the market pays a premium',
     'Hospitality, dining, tourism and lifestyle retail, with a resident base that supports '
     'higher price points and a visitor economy layered on top.',
     'Restaurants and bars, flagship retail, wellness and beauty, premium services, '
     'hospitality-adjacent concepts.',
     'Affluent residents plus a substantial seasonal and visitor population. Expectations '
     'around design, service and finish are visibly higher.',
     'Higher occupancy costs and higher build-out standards. Design review can be more '
     'involved than elsewhere in the valley.',
     'Old Town, the resort corridor and north Scottsdale behave like three different '
     'markets. Seasonality is real and needs to be modelled.',
     'A concept that depends on volume at a moderate price point can struggle to carry '
     'the occupancy cost.'),
    ('Tempe', 'The talent',
     'A dense, walkable, university-anchored city with a young population and a visible '
     'startup and technology presence.',
     'Technology and software, R&D functions, startups, casual dining and late-night food, '
     'student-facing retail and services.',
     'Students, recent graduates, young professionals and university staff — high density, '
     'lower average spend, high frequency.',
     'Limited land and a compact footprint. Space is competitive and generally smaller.',
     'Proximity to campus is a genuine variable, not a rounding error. So is the academic '
     'calendar.',
     'Summer and semester breaks change footfall substantially for consumer businesses.'),
    ('Mesa', 'Room to build',
     'The valley\'s industrial and logistics side, with aerospace activity around Falcon '
     'Field, more available land, and large expanding residential communities.',
     'Manufacturing, aerospace and defence suppliers, logistics and warehousing, light '
     'industrial, trades and construction services.',
     'A large residential base with a broad income range, plus industrial and commercial '
     'tenants as B2B customers.',
     'Generally lower cost per square foot than the western valley, with more options for '
     'larger footprints and build-to-suit.',
     'Access to freeways and to the airport matters more here than street-level visibility.',
     'Consumer concepts that need dense walk-in traffic may find the built environment too '
     'dispersed.'),
    ('Gilbert', 'The family market',
     'A large, fast-growing suburban community with strong household formation and an '
     'active town centre.',
     'Neighbourhood retail, family dining, health and education services, second locations '
     'for proven concepts.',
     'Families and households with stable incomes who shop and eat close to home.',
     'Newer commercial developments, generally well-maintained, with retail centres built '
     'around residential growth.',
     'Trade areas are residential and local. Regional draw is limited compared with '
     'Scottsdale or Tempe.',
     'A weaker choice for a first location that needs to attract customers from across the '
     'metro.'),
    ('Chandler', 'The technology corridor',
     'The most concentrated technology and advanced-manufacturing presence in the valley, '
     'with corporate offices and international supply-chain activity alongside it.',
     'Semiconductor supply chain, precision manufacturing, industrial services, B2B '
     'technology, corporate and engineering offices.',
     'Engineers, technical professionals and their households, plus a substantial base of '
     'corporate and industrial customers.',
     'Industrial and flex space oriented toward technical uses, with commercial development '
     'shaped around the employment base.',
     'Proximity to a specific customer or campus is often the deciding factor rather than '
     'general location quality.',
     'Industrial space near the main clusters is in demand, which affects both cost and '
     'timing.'),
]

CITIES_ZH = [
    ('Phoenix', '重心所在',
     '州政府、最大的雇主、機場，以及整個都會區的物流骨幹。市中心承載專業服務與公共機能；'
     '整座城市涵蓋範圍極大，內部條件差異也極大。',
     '專業服務、物流與配銷、總部機能、B2B 營運，以及服務商務旅客的接待業。',
     '全谷地最廣的客群組合——公部門、企業與住宅人口兼具，所得區間依區域差異很大。',
     '商用空間存量最深、價格帶最廣，證照與審查體系也最成熟。',
     '各區差異極大。相隔五分鐘車程的兩個地址，可能代表完全不同的商圈、客群與租金。',
     '規模是雙面刃：很容易選到一個名義上在 Phoenix、實際上卻落在錯誤市場的位置。'),
    ('Scottsdale', '願意付出溢價的市場',
     '以接待、餐飲、觀光與生活風格零售為主，居民本身支撐得起較高價位，上面又疊了一層'
     '訪客經濟。',
     '餐廳與酒吧、旗艦零售、健康與美容、高端服務，以及與接待業相鄰的業態。',
     '高所得居民，加上可觀的季節性與觀光人口。對設計、服務與完成度的期待明顯較高。',
     '租金與裝修標準都比較高。設計審查的程序也可能比谷地其他城市更繁複。',
     'Old Town、度假村廊帶與北 Scottsdale 幾乎是三個不同市場。季節性是真實存在的，'
     '必須納入財務模型。',
     '如果你的概念是靠中價位走量，租金負擔可能撐不住。'),
    ('Tempe', '人才所在',
     '一座密度高、適合步行、以大學為核心的城市，人口年輕，新創與科技能量明顯。',
     '科技與軟體、研發機能、新創、輕食與宵夜餐飲，以及面向學生的零售與服務。',
     '學生、社會新鮮人、年輕專業人士與大學教職員——密度高、客單價偏低、消費頻率高。',
     '土地有限、範圍緊湊，空間競爭激烈且坪數普遍較小。',
     '離校園多近是真實的變數，不是可以四捨五入的細節；學期行事曆同樣是。',
     '暑假與學期之間的空檔，會讓消費型業態的來客數出現明顯落差。'),
    ('Mesa', '還有空間可以蓋',
     '谷地的工業與物流面，Falcon Field 周邊有航太活動，土地供給較充裕，住宅社區也在'
     '持續擴張。',
     '製造業、航太與國防供應商、物流倉儲、輕工業，以及營建與技術工程服務。',
     '龐大的住宅人口、所得區間寬廣，另有工業與商業租戶作為 B2B 客群。',
     '單位面積成本普遍低於西谷地，大坪數與客製化建置的選項也更多。',
     '這裡的重點是高速公路與機場的可及性，而不是臨街能見度。',
     '需要密集步行人流的消費型業態，可能會覺得這裡的建成環境太分散。'),
    ('Gilbert', '家庭市場',
     '規模大、成長快的郊區社區，家戶形成穩健，並有一個活絡的城鎮中心。',
     '社區型零售、家庭餐飲、健康與教育服務，以及已驗證概念的第二據點。',
     '所得穩定的家庭與家戶，消費與用餐習慣以住家附近為主。',
     '商業開發較新、維護良好，零售中心多半是配合住宅成長而興建。',
     '商圈屬性偏住宅與在地，跨區吸引力不如 Scottsdale 或 Tempe。',
     '如果第一個據點就需要吸引整個都會區的客人，這裡不是好選擇。'),
    ('Chandler', '科技廊帶',
     '谷地內科技與先進製造最集中的區域，同時聚集企業辦公室與國際供應鏈活動。',
     '半導體供應鏈、精密製造、工業服務、B2B 科技，以及企業與工程辦公室。',
     '工程師、技術專業人士與其家庭，另有可觀的企業與工業客戶基礎。',
     '空間類型偏向工業與彈性廠辦，商業開發也是圍繞就業人口而形成。',
     '決定因素通常是「離某個特定客戶或園區多近」，而不是位置本身的一般條件。',
     '主要聚落周邊的工業空間需求旺盛，這會同時影響成本與時程。'),
]


def city_blocks(cities, labels):
    out = []
    for name, role, character, industries, customer, commercial, location, limits in cities:
        out.append(('h2', f'{name} — {role}'))
        out.append(('p', character))
        out.append(('ul', [
            f'<strong>{labels[0]}</strong> {industries}',
            f'<strong>{labels[1]}</strong> {customer}',
            f'<strong>{labels[2]}</strong> {commercial}',
            f'<strong>{labels[3]}</strong> {location}',
            f'<strong>{labels[4]}</strong> {limits}',
        ]))
    return out


PAGES['phoenix-metro-market-guide'] = {
    'type': 'article', 'hero': 'hero-metro-guide.jpg',
    'related': ['opening-a-restaurant-in-arizona', 'taiwanese-consumer-brand-us-market-entry'],
    'en': dict(
        category='City Guide', readingTime='11 min read',
        published='2026-08-06', updated='2026-08-06', dateLabel='August 2026',
        crumb='Phoenix Metro market guide',
        title='Phoenix Metro Market Guide: Choosing the Right City',
        desc='Phoenix, Scottsdale, Tempe, Mesa, Gilbert and Chandler serve different '
             'customers, industries and business models. A practical comparison for '
             'companies deciding where to land.',
        heroAlt='A Greater Phoenix city centre at sunset',
        cardBlurb='Six cities, one valley, and the variables that decide between them.',
        standfirst='Greater Phoenix is not one market. It is a set of adjacent cities with '
                   'genuinely different customers, cost structures and commercial characters '
                   '— and choosing the wrong one is among the most expensive mistakes a new '
                   'arrival can make.',
        body=[
            ('p', 'From Taipei, the metro reads as a single dot on a map. On the ground it '
                  'behaves as six markets that happen to share a valley, an airport and a '
                  'freeway system. What follows is a working comparison — not a ranking. '
                  'There is no universally correct answer, and any consultant who gives you '
                  'one has not asked enough questions about your business.'),
            ('pull', 'The right address is not the best city. It is the city whose customers, '
                     'costs and constraints match the business you are actually running.', None),
        ] + city_blocks(CITIES_EN, [
            'Suitable for:', 'Customer profile:', 'Commercial environment:',
            'Location considerations:', 'Potential limitations:']) + [
            ('fig', 'city-tempe.jpg', 'The light rail corridor between Phoenix and Tempe',
             'The light rail corridor. Fifteen minutes apart can mean two municipalities, '
             'two permitting timelines and two different answers.'),
            ('h2', 'How to actually decide'),
            ('p', 'The choice depends on six variables, and they are rarely weighted equally. '
                  'Work through them in order and the field usually narrows to two cities '
                  'quickly.'),
            ('panel', 'How to decide', 'The six variables', [
                '<strong>Business model.</strong> Do you need footfall, proximity to a '
                'customer, land, or none of the above?',
                '<strong>Customers.</strong> Where do they live or operate, and how far will '
                'they travel for what you sell?',
                '<strong>Workforce.</strong> Which labour pool do you need, and can they '
                'reasonably commute to you?',
                '<strong>Budget.</strong> What does occupancy cost do to your unit economics '
                'in each candidate city?',
                '<strong>Logistics.</strong> How do goods reach you and leave you, and does '
                'freeway or airport access matter?',
                '<strong>Growth plan.</strong> Is this a first of several locations, and does '
                'this city support the second one?',
            ], 'If two cities still tie after this, walk both on a weekday and a weekend '
               'before deciding.'),
            ('h2', 'A note on how these differences show up in practice'),
            ('p', 'Two addresses fifteen minutes apart can sit in different municipalities, '
                  'with different permitting timelines, different design review processes and '
                  'different answers to the same question. That is not a detail — for a '
                  'build-out it can be the difference between opening in month nine and month '
                  'fourteen.'),
            ('advisory', ADV_EN),
        ],
    ),
    'zh-tw': dict(
        category='城市指南', readingTime='閱讀時間 11 分鐘',
        published='2026-08-06', updated='2026-08-06', dateLabel='2026 年 8 月',
        crumb='鳳凰城都會區市場指南',
        title='鳳凰城都會區市場指南：如何選擇適合企業落地的城市？',
        desc='Phoenix、Scottsdale、Tempe、Mesa、Gilbert 與 Chandler 服務的客群、產業與'
             '商業模式各不相同。給正在決定落腳位置的企業一份實務比較。',
        heroAlt='黃昏時分的大鳳凰城市中心',
        cardBlurb='六座城市、一個谷地，以及決定該選哪一個的變數。',
        standfirst='大鳳凰城不是單一市場，而是一組相鄰的城市，各自有真實不同的客群、成本結構與'
                   '商業性格——選錯城市，是新進者最昂貴的錯誤之一。',
        body=[
            ('p', '從台北看，這個都會區在地圖上只是一個點。到了現場，它其實是六個共用一座谷地、'
                  '一座機場與一套高速公路系統的市場。以下是實務比較，不是排名。這個問題沒有'
                  '普世正確答案；如果有顧問直接給你一個，那代表他問你的問題還不夠多。'),
            ('pull', '對的地址不是「最好的城市」，而是客群、成本與限制條件，'
                     '剛好符合你正在經營的這門生意的那一座。', None),
        ] + city_blocks(CITIES_ZH, [
            '適合業態：', '客群樣貌：', '商業環境：',
            '選址考量：', '可能的限制：']) + [
            ('fig', 'city-tempe.jpg', 'Phoenix 與 Tempe 之間的輕軌廊帶',
             '輕軌廊帶。相隔十五分鐘車程，可能就是兩個市政區、兩套證照時程、兩種答案。'),
            ('h2', '實際上該怎麼決定'),
            ('p', '這個選擇取決於六個變數，而它們的權重通常並不相等。照順序走一遍，'
                  '候選城市多半會很快收斂到兩個。'),
            ('panel', '如何決定', '六個變數', [
                '<strong>商業模式。</strong>你需要的是人流、鄰近特定客戶、土地，還是以上皆非？',
                '<strong>客群。</strong>他們住在哪裡或在哪裡營運？為了你賣的東西，他們願意'
                '移動多遠？',
                '<strong>人力。</strong>你需要哪一種勞動力？他們通勤到你這裡合理嗎？',
                '<strong>預算。</strong>在每個候選城市，租金與裝修成本會如何改變你的單店損益？',
                '<strong>物流。</strong>貨怎麼進來、怎麼出去？高速公路或機場的可及性重要嗎？',
                '<strong>成長規劃。</strong>這是多個據點裡的第一個嗎？這座城市撐得起第二個嗎？',
            ], '如果走完還是兩個城市平手，請分別在平日與週末各走一趟，再做決定。'),
            ('h2', '這些差異在實務上怎麼出現'),
            ('p', '相隔十五分鐘車程的兩個地址，可能分屬不同市政區，有不同的證照時程、'
                  '不同的設計審查程序，對同一個問題也會給出不同答案。這不是細節——'
                  '對需要施工的業態來說，它可能就是第九個月開幕和第十四個月開幕的差別。'),
            ('advisory', ADV_ZH),
        ],
    ),
}

# ═══════════════════════════════════════════════════════════════════════════
# ARTICLE 03
# ═══════════════════════════════════════════════════════════════════════════
PAGES['first-steps-before-us-expansion'] = {
    'type': 'article', 'hero': 'hero-first-steps.jpg',
    'related': ['arizona-gateway-for-taiwanese-companies', 'phoenix-metro-market-guide'],
    'en': dict(
        category='Practical Guide', readingTime='10 min read',
        published='2026-08-06', updated='2026-08-06', dateLabel='August 2026',
        crumb='First steps before expanding',
        title='The First Steps Before Expanding into the U.S.',
        desc='What to clarify, validate and prepare before incorporating in the United '
             'States — purpose, business model, advisors, budget, localization and a phased '
             'market-entry roadmap.',
        heroAlt='Mixed-use development in midtown Phoenix',
        cardBlurb='What has to be true before you incorporate, hire or sign anything.',
        standfirst='Most expansions do not fail at execution. They fail because a decision '
                   'was made before the question underneath it was answered — and the cost of '
                   'that shows up eighteen months later, in a lease, a hire, or a structure '
                   'that no longer fits.',
        body=[
            ('h2', 'Clarify the purpose of expansion'),
            ('p', 'Before anything else, be specific about why. Following a customer into a '
                  'market is a different project from testing a new consumer market, which is '
                  'different again from establishing a legal presence for procurement, '
                  'investment or credibility. Each implies a different structure, a different '
                  'budget and a different definition of success.'),
            ('p', 'Write the reason down in one sentence. If the sentence needs an "and", you '
                  'may be attempting two projects at once — which is possible, but should be '
                  'a decision rather than an accident.'),
            ('h2', 'Validate the market before you incorporate'),
            ('p', 'Incorporation feels like progress, which is exactly why it is so often done '
                  'too early. An entity creates filing obligations, accounting work and, '
                  'frequently, a sense of commitment that makes later course correction '
                  'harder. Validation is cheaper first: customer conversations, competitor '
                  'observation on the ground, pricing tests, and an honest read on whether '
                  'the value proposition survives translation.'),
            ('h2', 'Define the U.S. business model'),
            ('p', 'The same company can enter the U.S. as a direct operator, through a '
                  'distributor, via licensing, as a joint venture, or as a subsidiary '
                  'supplying an existing customer. These are not interchangeable. They imply '
                  'different capital requirements, different control, different tax treatment '
                  'and different exit options.'),
            ('h2', 'Company structure and professional advisors'),
            ('p', 'Structure is where the accountant and the attorney disagree productively, '
                  'and where a founder should be present rather than delegating. The choice '
                  'of entity type, state of formation, ownership structure and intercompany '
                  'arrangements will shape your tax position and your flexibility for years.'),
            ('p', 'Engage advisors before you need them. A CPA and an attorney who have '
                  'handled Taiwan–U.S. structures before will save you more than they cost in '
                  'the first year alone.'),
            ('advisory', ADV_EN),
            ('h2', 'Legal, accounting, tax, insurance and immigration coordination'),
            ('p', 'These five workstreams interact. Entity choice affects tax treatment; tax '
                  'treatment affects how you compensate people; how you compensate people '
                  'affects insurance and payroll; and any plan involving someone from Taiwan '
                  'working in the U.S. has its own separate requirements and timelines.'),
            ('p', 'The practical failure mode is sequencing them one at a time and discovering '
                  'in month six that decision two has constrained decision five. Get all five '
                  'advisors in one conversation early, even briefly.'),
            ('pull', 'Incorporation feels like progress. That is exactly why it is so often '
             'done too early.', None),
            ('h2', 'Brand localization'),
            ('p', 'Localization is not translation. It covers the name and whether it is '
                  'pronounceable and available; the positioning and whether it means anything '
                  'to an American customer; the packaging, labelling and claims; the visual '
                  'identity; and the story you tell about where you come from — which is often '
                  'an asset rather than something to minimise.'),
            ('h2', 'Budget and cash-flow preparation'),
            ('p', 'Two numbers matter more than the total: how much you will spend before '
                  'there is any revenue, and how long that period lasts. Build the model with '
                  'a conservative revenue ramp and a realistic build-out timeline, then add '
                  'contingency for the permitting and construction schedule you do not control.'),
            ('h2', 'Local partner evaluation'),
            ('p', 'Whether it is a distributor, a landlord, a contractor or an operating '
                  'partner, evaluate on three things: have they done this specific thing '
                  'before, can you speak to someone they did it for, and are their incentives '
                  'aligned with yours or with the other side of the table?'),
            ('fig', 'hero-metro-guide.jpg', 'A Greater Phoenix city centre at sunset',
             'Site selection should follow the business model, not lead it.'),
            ('h2', 'Site selection and operational planning'),
            ('p', 'Site selection should follow the business model, not lead it. Once the '
                  'model is fixed, the questions become concrete: which city, which trade '
                  'area, what size, what condition, what timeline, and what does the space '
                  'need to be capable of on day one versus year three?'),
            ('h2', 'Build a phased market-entry roadmap'),
            ('p', 'A roadmap that treats entry as one event will break. A phased plan — '
                  'validate, establish, prepare, launch, operate — allows each phase to be '
                  'funded and reviewed on its own terms, and allows you to stop between '
                  'phases without having written off everything.'),
            ('h2', 'Common mistakes to avoid'),
            ('ul', [
                'Incorporating before validating, then feeling committed to a market you have '
                'not tested.',
                'Underestimating the time between signing a lease and opening a door.',
                'Hiring a technical first employee when the business needed a manager who can '
                'read a lease and a payroll report.',
                'Choosing a city from a map rather than from a visit.',
                'Assuming a supplier relationship transfers automatically to a U.S. entity.',
                'Budgeting for construction but not for the months of payroll and rent before '
                'revenue.',
                'Treating professional advisors as a cost to minimise rather than the '
                'foundation everything else sits on.',
            ]),
            ('panel', 'Key takeaways', 'Practical preparation checklist', [
                'One-sentence statement of why you are expanding.',
                'Written U.S. business model, with the alternatives you rejected and why.',
                'Market validation evidence — conversations, observations, pricing tests.',
                'CPA and attorney engaged, structure agreed in writing.',
                'Five-workstream review completed: legal, accounting, tax, insurance, '
                'immigration.',
                'Brand localization decisions documented, including name and claims.',
                'Cash-flow model covering the pre-revenue period plus contingency.',
                'Shortlist of two cities, both visited on the ground.',
                'Named professional advisors and at least one reference each.',
                'Phased roadmap with a defined stop point between each phase.',
            ], 'You do not need every line complete before you move. You do need to know '
               'which ones are not.'),
        ],
    ),
    'zh-tw': dict(
        category='實務指南', readingTime='閱讀時間 10 分鐘',
        published='2026-08-06', updated='2026-08-06', dateLabel='2026 年 8 月',
        crumb='進入美國市場前的準備',
        title='進入美國市場前，企業應該先完成哪些準備？',
        desc='在美國設立公司之前，該先釐清、驗證與準備什麼——目的、商業模式、專業顧問、預算、'
             '品牌在地化，以及分階段的市場進入路線圖。',
        heroAlt='Phoenix 中城的複合式開發街區',
        cardBlurb='在你設立公司、聘人或簽下任何文件之前，有哪些事必須先成立。',
        standfirst='多數的海外拓展，失敗的不是執行，而是在底層問題還沒被回答之前就先做了決定。'
                   '代價會在十八個月後才出現——在一紙租約、一個人事案，或一個已經不合身的架構上。',
        body=[
            ('h2', '先把「為什麼」講清楚'),
            ('p', '在做任何事之前，先具體說明目的。跟著客戶進入一個市場，和測試一個新的消費市場，'
                  '是完全不同的專案；而為了採購、投資或商業信任度而建立法律實體，又是另一回事。'
                  '三者對應的架構、預算與成功定義都不一樣。'),
            ('p', '把理由寫成一句話。如果這句話需要用到「而且」，你可能同時在做兩個專案——'
                  '這是可行的，但應該是一個決定，而不是一個意外。'),
            ('h2', '設立公司之前，先驗證市場'),
            ('p', '設立公司會讓人覺得「有在前進」，這正是它常常被太早執行的原因。一個法律實體'
                  '會帶來申報義務、帳務工作，而且往往會產生一種承諾感，讓後續修正方向變得更難。'
                  '先做驗證便宜得多：與潛在客戶對話、在現場觀察競爭者、測試定價，'
                  '並誠實判斷你的價值主張經過語境轉換之後是否還成立。'),
            ('h2', '定義你的美國商業模式'),
            ('p', '同一家公司可以用直營、經銷、授權、合資，或作為既有客戶的供應子公司等方式'
                  '進入美國。這些不能互相替換——它們對應不同的資金需求、不同的控制權、'
                  '不同的稅務處理，以及不同的退場選項。'),
            ('h2', '公司架構與專業顧問'),
            ('p', '架構是會計師與律師會有建設性分歧的地方，也是創辦人應該親自在場、'
                  '而非全權授權的地方。實體型態、設立州別、股權結構與集團內部安排，'
                  '會在未來好幾年影響你的稅務地位與彈性。'),
            ('p', '在需要之前就先找顧問。一位處理過台美架構的會計師與律師，'
                  '光是第一年幫你省下的，就會超過他們的費用。'),
            ('advisory', ADV_ZH),
            ('h2', '法律、會計、稅務、保險與移民的協調'),
            ('p', '這五條工作線會互相牽動。實體型態影響稅務處理；稅務處理影響你怎麼給付人員；'
                  '給付方式影響保險與薪資作業；而任何牽涉到台灣人員在美國工作的規劃，'
                  '都有自己獨立的要求與時程。'),
            ('p', '實務上最常見的失敗模式，是一條一條依序處理，然後在第六個月發現第二個決定'
                  '已經限制了第五個決定。盡早把五位顧問拉進同一場對話，哪怕只是短短一次。'),
            ('pull', '設立公司會讓人覺得「有在前進」——這正是它常常被太早執行的原因。', None),
            ('h2', '品牌在地化'),
            ('p', '在地化不是翻譯。它包含名稱是否好唸、是否可註冊；定位對美國消費者是否有意義；'
                  '包裝、標示與宣稱；視覺識別；以及你如何講述自己從哪裡來——'
                  '這件事通常是資產，而不是需要淡化的東西。'),
            ('h2', '預算與現金流準備'),
            ('p', '有兩個數字比總額更重要：在有營收之前你會花掉多少，以及那段期間有多長。'
                  '用保守的營收爬升曲線與務實的施工時程建立模型，再為你無法控制的'
                  '證照與工程排程加上緩衝。'),
            ('h2', '評估在地夥伴'),
            ('p', '不論對象是經銷商、房東、承包商或營運夥伴，都用三件事評估：'
                  '他們做過這件「特定的事」嗎？你能不能跟他們服務過的對象直接談？'
                  '他們的誘因是站在你這一邊，還是桌子的另一邊？'),
            ('fig', 'hero-metro-guide.jpg', '黃昏時分的大鳳凰城市中心',
             '選址應該跟著商業模式走，而不是反過來。'),
            ('h2', '選址與營運規劃'),
            ('p', '選址應該跟著商業模式走，而不是反過來。模式確定之後，問題就變得具體：'
                  '哪座城市、哪個商圈、多大坪數、什麼屋況、什麼時程，以及這個空間在'
                  '第一天與第三年分別需要具備什麼能力？'),
            ('h2', '建立分階段的市場進入路線圖'),
            ('p', '把「進入市場」當成單一事件的計畫一定會斷。分階段的規劃——驗證、設立、準備、'
                  '啟動、營運——讓每個階段可以各自編列預算、各自檢視，也讓你可以在階段之間'
                  '喊停，而不必把先前的投入全部一筆勾銷。'),
            ('h2', '常見的錯誤'),
            ('ul', [
                '先設立公司再驗證市場，然後對一個還沒測試過的市場產生承諾感。',
                '低估從簽下租約到開門營業之間的時間。',
                '第一個美國員工找了技術人才，但公司真正需要的是看得懂租約與薪資報表的管理者。',
                '從地圖上選城市，而不是實地走過再選。',
                '假設既有的供應關係會自動轉移到美國實體。',
                '編了施工預算，卻沒編營收之前那幾個月的薪資與租金。',
                '把專業顧問當成要壓低的成本，而不是其他一切賴以站立的基礎。',
            ]),
            ('panel', '重點整理', '出發前的實務檢核表', [
                '一句話說明你為什麼要拓展。',
                '書面的美國商業模式，並記錄你排除了哪些選項、為什麼。',
                '市場驗證的證據——對話紀錄、現場觀察、定價測試。',
                '已委任會計師與律師，架構有書面共識。',
                '完成五條工作線的通盤檢視：法律、會計、稅務、保險、移民。',
                '品牌在地化決策已記錄，包含名稱與產品宣稱。',
                '涵蓋無營收期的現金流模型，並含緩衝。',
                '收斂到兩座候選城市，且兩座都實地走過。',
                '每位專業顧問都有具體人選，且至少各有一組推薦人。',
                '分階段路線圖，且每個階段之間都有明確的停損點。',
            ], '你不需要在出發前把每一項都完成，但你需要知道哪幾項還沒完成。'),
        ],
    ),
}

# ═══════════════════════════════════════════════════════════════════════════
# ARTICLE 04
# ═══════════════════════════════════════════════════════════════════════════
PAGES['opening-a-restaurant-in-arizona'] = {
    'type': 'article', 'hero': 'hero-restaurant-guide.jpg',
    'related': ['phoenix-metro-market-guide', 'taiwanese-restaurant-group-exploring-phoenix'],
    'en': dict(
        category='Industry Guide', readingTime='12 min read',
        published='2026-08-06', updated='2026-08-06', dateLabel='August 2026',
        crumb='Opening a restaurant in Arizona',
        title='What Restaurant Brands Should Know Before Opening in Arizona',
        desc='Positioning, trade area, lease structure, kitchen planning, permits, '
             'construction, supply chain, hiring and launch — a practical orientation for '
             'restaurant brands entering the Arizona market.',
        heroAlt='Resort dining and pools at dusk in Scottsdale',
        cardBlurb='From trade area to soft opening: what decides whether the first year works.',
        standfirst='A restaurant is the hardest kind of first U.S. location: it combines real '
                   'estate, construction, licensing, perishable supply chain and hourly '
                   'labour, and every one of those can move your opening date. Here is the '
                   'shape of the work.',
        body=[
            ('h2', 'Market positioning and customer expectations'),
            ('p', 'The first question is not where, but for whom. A concept that works in '
                  'Taipei because of price, speed and familiarity may need a different frame '
                  'in Arizona, where the same food might be positioned as a discovery rather '
                  'than a routine. Portion expectations, service pace, tipping norms, dietary '
                  'labelling and alcohol attachment all shape the economics.'),
            ('h2', 'Choosing the right city and trade area'),
            ('p', 'City choice sets the ceiling on your price point and the shape of your '
                  'demand curve; trade area decides whether anyone walks in. Look at daypart '
                  'patterns, co-tenancy, parking, visibility and the actual drive time from '
                  'the residential areas your customers live in — not the radius on a map.'),
            ('h3', 'Second-generation space versus empty shell'),
            ('p', 'A second-generation restaurant space — one that was previously a restaurant '
                  '— arrives with grease interception, hood infrastructure, floor drains and '
                  'often a usable service layout. A shell arrives with none of it. The rent '
                  'difference rarely reflects the build-out difference, and for a first U.S. '
                  'location the shorter, more predictable path is usually worth paying for.'),
            ('h2', 'Commercial lease considerations'),
            ('p', 'Base rent is the least useful number in the negotiation. Look at the '
                  'structure — most U.S. commercial leases pass through property taxes, '
                  'insurance and common area maintenance — and then at the terms that actually '
                  'move the deal:'),
            ('ul', [
                '<strong>Tenant improvement allowance</strong> — the landlord\'s contribution '
                'to build-out, often more valuable to a restaurant than a rent reduction.',
                '<strong>Free rent</strong> during construction, which transfers your riskiest '
                'months back across the table.',
                '<strong>Annual escalations</strong>, which compound into a very different '
                'ten-year cost.',
                '<strong>Guarantee</strong> — a new U.S. entity has no credit history, so the '
                'Taiwanese parent will usually be asked to guarantee. How much and for how '
                'long is negotiable.',
                '<strong>Use clause and exclusivity</strong> — what you are permitted to sell, '
                'and whether a competitor can open next door.',
            ]),
            ('p', 'The broker showing you the space is usually paid by the landlord. A '
                  'tenant-side broker is paid from the same commission pool but represents '
                  'you. On a first lease, in a market you do not know, that is not an optional '
                  'cost.'),
            ('pull', 'For a restaurant, the tenant improvement allowance is often worth more '
                     'than the rent reduction you were negotiating for.', None),
            ('h2', 'Kitchen planning and equipment'),
            ('p', 'Kitchen design drives the permit set, the mechanical and plumbing scope, '
                  'and much of the construction budget. Equipment sourcing has lead times that '
                  'are easy to underestimate, and imported equipment may need to meet '
                  'recognised U.S. safety and sanitation certifications to pass inspection. '
                  'Confirm certification requirements before you ship anything.'),
            ('h2', 'Permits and professional review'),
            ('p', 'A restaurant build-out typically involves plan review, building permits, '
                  'health department review and, where alcohol is served, a separate licensing '
                  'process with its own timeline. Requirements and review speeds differ by '
                  'city and county. This is the single most common source of schedule slip and '
                  'it is largely outside your control — which is why it belongs at the front '
                  'of the plan, not the middle.'),
            ('advisory', ADV_EN),
            ('h2', 'Construction budget and timeline'),
            ('p', 'Build with a contingency you would be embarrassed to defend and you will '
                  'roughly be right. The variables that move budgets most are the condition of '
                  'the existing space, the mechanical and electrical scope, whether structural '
                  'work is triggered, and how many review cycles the plans go through. Track '
                  'the schedule against the licensing timeline, not against the contractor\'s '
                  'optimism.'),
            ('fig', 'ind-restaurant.jpg', 'Restaurant patio at dusk in the Phoenix area',
             'Front of house is the part everyone plans for. The opening date is usually '
             'decided behind it.'),
            ('h2', 'Food suppliers and cold-chain logistics'),
            ('p', 'Map your menu against what is actually available locally, what has to come '
                  'from elsewhere in the U.S., and what would have to be imported. For imported '
                  'ingredients, confirm labelling and compliance requirements early, and build '
                  'a fallback for anything with a single source. Cold-chain storage and '
                  'delivery frequency should be settled before the menu is final, not after.'),
            ('h2', 'Hiring and labour planning'),
            ('p', 'Hourly labour markets in the metro are competitive, and turnover in food '
                  'service is high everywhere. Plan for a training period before opening, a '
                  'management layer that can operate without you present, and payroll running '
                  'for weeks before the first guest arrives. Employment rules, wage '
                  'requirements and required insurance should be confirmed with a U.S. '
                  'employment professional.'),
            ('h2', 'Menu and brand localization'),
            ('p', 'Decide deliberately what stays and what adapts. The dishes that carry your '
                  'identity should generally stay intact; the ones that exist for local habit '
                  'in Taiwan may need replacing. Menu structure, naming, description length, '
                  'allergen information and price architecture all read differently to an '
                  'American guest.'),
            ('h2', 'Alcohol, food-safety and operational requirements'),
            ('p', 'Alcohol licensing is a separate process with its own application, review '
                  'and, often, community notification steps. Food-safety certification, '
                  'manager training requirements and inspection regimes are set locally. None '
                  'of these are difficult in isolation; all of them have lead times, and they '
                  'do not run in parallel as neatly as a project plan suggests.'),
            ('h2', 'Soft opening and launch preparation'),
            ('p', 'A soft opening exists to find the problems that only appear under real '
                  'service: kitchen throughput, ticket times, service flow, POS behaviour and '
                  'staffing ratios. Budget for it as a period of controlled loss rather than '
                  'early revenue, and give yourself enough of it to fix what it reveals.'),
            ('h2', 'Common mistakes'),
            ('ul', [
                'Signing a shell space because the rent looked better than a second-generation '
                'restaurant.',
                'Starting the alcohol licence application after construction rather than '
                'alongside it.',
                'Shipping equipment before confirming U.S. certification requirements.',
                'Setting an opening date publicly before plan review is complete.',
                'Hiring the kitchen before hiring the manager.',
                'Building the menu before confirming the supply chain that has to support it.',
                'Treating the soft opening as a marketing event rather than an operational one.',
            ]),
            ('panel', 'Key takeaways', 'Pre-entry checklist', [
                'Concept positioning written down, with the American customer described '
                'specifically.',
                'Two candidate cities and at least three candidate trade areas, all visited.',
                'Second-generation versus shell decision made with a build-out estimate for '
                'each.',
                'Tenant-side broker engaged.',
                'Kitchen layout drafted and equipment certification requirements confirmed.',
                'Permitting and licensing timeline mapped for the specific municipality.',
                'Construction budget with contingency, tracked against the licensing schedule.',
                'Supply chain mapped: local, domestic, imported — with fallbacks.',
                'Hiring plan including a pre-opening training period and payroll runway.',
                'Menu localization decisions documented.',
                'Soft opening period budgeted as controlled loss.',
            ], 'Requirements vary by city, county, property and concept. Confirm every '
               'regulatory item locally before you build against it.'),
        ],
    ),
    'zh-tw': dict(
        category='產業指南', readingTime='閱讀時間 12 分鐘',
        published='2026-08-06', updated='2026-08-06', dateLabel='2026 年 8 月',
        crumb='餐飲品牌進入亞利桑那',
        title='餐飲品牌進入亞利桑那市場前，需要了解哪些事情？',
        desc='定位、商圈、租約結構、廚房規劃、證照、施工、供應鏈、人力與試營運——'
             '給準備進入亞利桑那市場的餐飲品牌一份實務指引。',
        heroAlt='黃昏時分 Scottsdale 的度假餐飲與泳池',
        cardBlurb='從商圈選擇到試營運：決定第一年成敗的那些事。',
        standfirst='餐廳是最難的一種美國首店：它同時牽涉不動產、施工、證照、生鮮供應鏈與時薪人力，'
                   '而其中任何一項都可能推遲你的開幕日。以下是這件事的實際形狀。',
        body=[
            ('h2', '市場定位與顧客期待'),
            ('p', '第一個問題不是「在哪裡」，而是「為了誰」。一個在台北靠價格、速度與熟悉感'
                  '成立的概念，到了亞利桑那可能需要換一個框架——同樣的料理，在這裡也許會被'
                  '定位成一次探索，而不是一種日常。份量期待、上菜節奏、小費文化、'
                  '飲食標示與酒水附加率，都會直接改變單店經濟結構。'),
            ('h2', '選擇城市與商圈'),
            ('p', '城市決定你的價格帶上限與需求曲線的形狀；商圈決定到底有沒有人走進來。'
                  '要看的是時段結構、鄰近業種組合、停車、能見度，以及從你客人實際居住的'
                  '住宅區開車過來的真實時間——不是地圖上的半徑。'),
            ('h3', '二手餐廳空間 vs. 毛胚屋'),
            ('p', '所謂二手餐廳空間，是指前一手就是餐廳的物件，通常已經有截油設施、'
                  '排煙管道、地板排水，而且往往有可用的動線配置。毛胚屋則什麼都沒有。'
                  '租金差價很少能反映裝修成本的差距——對第一間美國店來說，'
                  '那條比較短、比較可預測的路，通常值得多付一點。'),
            ('h2', '商用租約要看什麼'),
            ('p', '基本租金是整場談判中最沒用的數字。先看結構——多數美國商用租約會把'
                  '房屋稅、保險與公共區域維護轉嫁給承租人——然後看真正會左右成交的條件：'),
            ('ul', [
                '<strong>裝修補助（TI allowance）</strong>——房東對裝修的補貼，'
                '對餐廳而言常常比減租更有價值。',
                '<strong>免租期</strong>——施工期間的免租，等於把你風險最高的那幾個月'
                '轉回桌子對面。',
                '<strong>年調幅</strong>——複利之後，十年總成本會差很多。',
                '<strong>保證</strong>——新設的美國實體沒有信用紀錄，房東通常會要求台灣母公司'
                '提供保證。金額多少、保多久，都是可以談的。',
                '<strong>使用條款與排他條款</strong>——你被允許賣什麼，以及競爭者能不能'
                '開在隔壁。',
            ]),
            ('p', '帶你看物件的經紀人，通常是房東付錢的。承租方經紀人從同一筆佣金中拆帳，'
                  '但代表的是你。在你還不熟悉的市場簽第一份租約時，這不是可選項。'),
            ('pull', '對餐廳來說，裝修補助的價值，往往超過你正在爭取的那筆減租。', None),
            ('h2', '廚房規劃與設備'),
            ('p', '廚房設計會決定送審圖說、機電與給排水的範圍，以及大部分的施工預算。'
                  '設備採購的前置期很容易被低估；而進口設備可能需要符合美國認可的'
                  '安全與衛生認證才能通過查驗。出貨之前，先確認認證要求。'),
            ('h2', '證照與專業審查'),
            ('p', '餐廳裝修通常會涉及圖說審查、建築執照、衛生局審查；若要供應酒精，'
                  '還有一套獨立的執照流程與時程。各城市與郡的要求與審查速度都不同。'
                  '這是時程延誤最常見的來源，而且大部分不在你的控制範圍內——'
                  '正因如此，它應該排在計畫的最前面，不是中間。'),
            ('advisory', ADV_ZH),
            ('h2', '施工預算與時程'),
            ('p', '把緩衝抓到一個你自己講出來會有點不好意思的數字，大概就對了。'
                  '最會影響預算的變數是：既有空間的屋況、機電範圍、是否觸發結構工程，'
                  '以及圖說跑了幾輪審查。追蹤時程時，請對照證照的時間軸，'
                  '而不是承包商的樂觀預估。'),
            ('fig', 'ind-restaurant.jpg', '鳳凰城地區餐廳庭院的黃昏景象',
             '外場是每個人都會規劃的部分，但開幕日期通常是在它後面被決定的。'),
            ('h2', '食材供應與冷鏈'),
            ('p', '把菜單逐項對照：哪些在地就能取得、哪些要從美國其他地方調度、'
                  '哪些必須進口。進口食材要及早確認標示與法規要求，'
                  '並為任何單一來源的品項準備備案。冷藏倉儲與配送頻率應該在菜單定案「之前」'
                  '就確定，而不是之後。'),
            ('h2', '人力招募與規劃'),
            ('p', '大鳳凰城的時薪人力市場競爭激烈，而餐飲業的流動率在哪裡都很高。'
                  '請預留開幕前的訓練期、一層不需要你在場也能運作的管理層，'
                  '以及第一位客人上門之前就要開始跑的數週薪資。'
                  '雇傭規定、薪資要求與必要保險，請與美國的勞動法務專業人士確認。'),
            ('h2', '菜單與品牌在地化'),
            ('p', '要刻意決定什麼留下、什麼調整。承載你身分認同的那幾道菜通常應該原樣保留；'
                  '而那些只是因應台灣在地習慣而存在的品項，可能需要替換。菜單結構、命名、'
                  '敘述長度、過敏原資訊與價格架構，在美國客人眼中的閱讀方式都不一樣。'),
            ('h2', '酒精、食安與營運規定'),
            ('p', '酒類執照是一套獨立流程，有自己的申請、審查，往往還有社區公告程序。'
                  '食安認證、店長訓練要求與查驗制度則由地方訂定。單獨看每一項都不困難；'
                  '但每一項都有前置期，而且它們不會像專案計畫上畫的那樣漂亮地平行進行。'),
            ('h2', '試營運與開幕準備'),
            ('p', '試營運的目的，是找出只有在真實出餐狀態下才會出現的問題：'
                  '廚房產能、出餐時間、服務動線、POS 行為與人力配比。'
                  '請把它當成一段「可控的虧損期」來編預算，而不是提早的營收，'
                  '並且給自己足夠長的時間，去修正它揭露出來的東西。'),
            ('h2', '常見的錯誤'),
            ('ul', [
                '因為租金看起來比二手餐廳空間便宜，就簽下毛胚屋。',
                '施工結束後才開始申請酒類執照，而不是同步進行。',
                '在確認美國認證要求之前就把設備寄出。',
                '在圖說審查完成之前就對外公布開幕日期。',
                '先招廚房、後招管理者。',
                '在確認能支撐它的供應鏈之前就把菜單定案。',
                '把試營運當成行銷活動，而不是營運壓力測試。',
            ]),
            ('panel', '重點整理', '進入市場前的檢核表', [
                '概念定位已書面化，並具體描述了美國客群。',
                '兩座候選城市、至少三個候選商圈，且全部實地走過。',
                '二手空間與毛胚屋的取捨已決定，且各有裝修成本估算。',
                '已委任承租方經紀人。',
                '廚房配置已初步繪製，設備認證要求已確認。',
                '已針對特定市政區盤點證照與執照時程。',
                '施工預算含緩衝，並對照證照時間軸追蹤。',
                '供應鏈已盤點：在地、美國境內、進口，並備妥替代方案。',
                '人力計畫含開幕前訓練期與薪資撐持期。',
                '菜單在地化決策已記錄。',
                '試營運期已列為可控虧損並編入預算。',
            ], '各項規定會因城市、郡、物件與業態而不同。任何法規事項，'
               '都請在依據它施工之前先於當地確認。'),
        ],
    ),
}

# ═══════════════════════════════════════════════════════════════════════════
# PROJECT 01
# ═══════════════════════════════════════════════════════════════════════════
PAGES['taiwanese-restaurant-group-exploring-phoenix'] = {
    'type': 'project', 'hero': 'hero-restaurant-project.jpg',
    'related': ['opening-a-restaurant-in-arizona', 'phoenix-metro-market-guide'],
    'en': dict(
        category='Food & Beverage', status='Market Exploration · In Progress', statusShort='Market Exploration',
        industry='Food & Beverage', dateLabel='August 2026',
        crumb='Restaurant group exploring Phoenix',
        title='Taiwanese Restaurant Group Exploring Phoenix',
        desc='An ongoing market exploration for a Taiwanese restaurant group evaluating '
             'Greater Phoenix — site visits, trade-area research, government and professional '
             'introductions, and supply-chain assessment.',
        heroAlt='Restaurant patio and pool at dusk in the Phoenix area',
        cardBlurb='Market visits, site selection research and supply-chain assessment, '
                  'currently underway.',
        standfirst='A Taiwanese restaurant group is evaluating Greater Phoenix as a potential '
                   'first U.S. market. The engagement is at the exploration stage: no site has '
                   'been selected, no lease has been signed, and no opening date exists.',
        facts=[('Status', 'Market Exploration · In Progress'),
               ('Industry', 'Food & Beverage'),
               ('Market', 'Greater Phoenix, Arizona'),
               ('Current phase', 'Site and trade-area research')],
        body=[
            ('h2', 'Background'),
            ('p', 'The client operates an established restaurant business in Taiwan and is '
                  'considering the United States as its first international market. The brand '
                  'is not named here; it will be identified publicly only if and when the '
                  'client approves.'),
            ('p', 'The group approached the question the right way round: rather than '
                  'selecting a location and then justifying it, they asked whether the U.S. '
                  'market makes sense for their concept at all, and if so, where.'),
            ('h2', 'Business objective'),
            ('p', 'To determine whether Greater Phoenix can support the concept at a viable '
                  'price point, and to identify the city and trade area that would give a '
                  'first location the best chance — or to conclude that the timing or the '
                  'market is wrong.'),
            ('h2', 'Market opportunity'),
            ('p', 'Greater Phoenix offers a large metropolitan consumer base with sub-markets '
                  'that differ substantially in income, density and dining behaviour. For a '
                  'restaurant concept, that variety is the opportunity: the same brand can '
                  'succeed or fail depending on which of those sub-markets it lands in.'),
            ('p', 'Build-out and occupancy conditions in the metro have historically been more '
                  'forgiving than a coastal debut, which changes what a first location can be '
                  'attempted on.'),
            ('pull', 'The goal is not to open quickly. The goal is to choose the right '
             'market.', None),
            ('h2', 'Current progress'),
            ('ul', [
                'Market visits across multiple Phoenix Metro cities, observing dayparts and '
                'trade areas in person.',
                'Research on restaurant and retail districts, including co-tenancy patterns '
                'and competitive density.',
                'Meetings with local government and economic-development resources to '
                'understand municipal requirements.',
                'Introductions to legal and accounting professionals experienced with '
                'cross-border structures.',
                'Early conversations with construction and permitting resources about '
                'realistic build-out timelines.',
                'Assessment of food suppliers, cold-chain logistics and warehousing options.',
                'Observation of local consumer behaviour and competitor positioning.',
            ]),
            ('advisory', 'Nothing in this engagement has been finalised. No site has been '
                         'selected, no lease negotiated, no permit filed and no opening '
                         'scheduled. All regulatory and licensing matters will be confirmed '
                         'with qualified U.S. professionals before any commitment is made.'),
            ('fig', 'city-scottsdale.jpg', 'Scottsdale, Arizona',
             'Scottsdale. One of several sub-markets under evaluation — each with a different '
             'customer and a different cost base.'),
            ('h2', "CnC Venture's role"),
            ('p', 'We coordinate the exploration itself: structuring the visit programme so '
                  'that the group sees comparable conditions across cities rather than a '
                  'curated tour, arranging introductions to government resources and '
                  'professional advisors, and assembling the market and supply-chain research '
                  'that the decision will rest on.'),
            ('p', 'We also hold the honest position. If the conclusion is that the concept '
                  'needs a different market, a different format or a later year, that is the '
                  'conclusion we deliver.'),
            ('h2', 'Next phase'),
            ('p', 'Narrowing to a shortlist of trade areas, developing comparative build-out '
                  'and occupancy scenarios, and determining the appropriate entry timing. Only '
                  'after that would site negotiation begin.'),
            ('panel', 'Key takeaways', 'What this engagement turns on', [
                'Whether the concept translates without losing what makes it distinctive.',
                'Second-generation restaurant space versus shell, and what each implies for '
                'timeline and budget.',
                'The permitting and licensing sequence in the specific municipality chosen.',
                'Supply-chain reliability for ingredients that cannot be sourced locally.',
                'Labour availability and the management layer required to operate at distance.',
                'The realistic length of the pre-revenue period.',
            ]),
        ],
    ),
    'zh-tw': dict(
        category='餐飲品牌', status='市場探索 · 進行中', statusShort='市場探索',
        industry='餐飲品牌', dateLabel='2026 年 8 月',
        crumb='台灣餐飲品牌鳳凰城評估',
        title='台灣餐飲品牌鳳凰城市場拓展評估',
        desc='一項進行中的市場探索：協助台灣餐飲集團評估大鳳凰城——實地考察、商圈研究、'
             '政府與專業顧問引薦，以及供應鏈評估。',
        heroAlt='鳳凰城地區餐廳庭院與泳池的黃昏景象',
        cardBlurb='實地考察、選址研究與供應鏈評估，目前進行中。',
        standfirst='一家台灣餐飲集團正在評估大鳳凰城作為其第一個美國市場的可能性。'
                   '目前處於探索階段：尚未選定地點、尚未簽署租約，也還沒有開幕時間。',
        facts=[('狀態', '市場探索 · 進行中'),
               ('產業', '餐飲品牌'),
               ('市場', '亞利桑那州・大鳳凰城'),
               ('目前階段', '選址與商圈研究')],
        body=[
            ('h2', '背景'),
            ('p', '客戶在台灣經營已具規模的餐飲事業，正考慮以美國作為第一個海外市場。'
                  '本頁不揭露品牌名稱；只有在客戶同意之後，才會對外具名。'),
            ('p', '這家集團把問題的順序擺對了：他們不是先選定地點再回頭合理化，'
                  '而是先問「美國市場對這個概念本身是否成立」，然後才問「如果成立，在哪裡」。'),
            ('h2', '事業目標'),
            ('p', '判斷大鳳凰城能否在可行的價格帶上支撐這個概念，並找出最能給第一間店'
                  '成功機會的城市與商圈——或者，得出「時機或市場不對」的結論。'),
            ('h2', '市場機會'),
            ('p', '大鳳凰城擁有龐大的都會消費人口，而各個次市場在所得、密度與外食習慣上'
                  '差異很大。對餐飲概念而言，這種多樣性本身就是機會：同一個品牌，'
                  '落在不同的次市場，結果可能完全不同。'),
            ('p', '這個都會區的裝修與租金條件，長期以來也比在沿海城市首發來得寬容，'
                  '這會改變第一間店可以嘗試的規模。'),
            ('pull', '目標不是快點開幕，而是選對市場。', None),
            ('h2', '目前進度'),
            ('ul', [
                '跨大鳳凰城多個城市的實地考察，親自觀察不同時段的商圈樣貌。',
                '餐飲與零售商圈研究，包含鄰近業種組合與競爭密度。',
                '與地方政府及經濟發展單位會面，理解各市政區的實際要求。',
                '引薦具跨境架構經驗的法律與會計專業人士。',
                '與營造及證照相關資源初步接觸，了解合理的施工時程。',
                '評估食材供應商、冷鏈物流與倉儲方案。',
                '觀察在地消費行為與競爭者定位。',
            ]),
            ('advisory', '本專案中沒有任何事項已經定案。尚未選定地點、未進行租約談判、'
                         '未送出任何證照申請，也沒有排定開幕。所有法規與證照事項，'
                         '都會在做出任何承諾之前，與具備資格的美國專業人士確認。'),
            ('fig', 'city-scottsdale.jpg', '亞利桑那州 Scottsdale',
             'Scottsdale。評估中的次市場之一——每一個都對應不同的客群與不同的成本結構。'),
            ('h2', 'CnC Venture 的角色'),
            ('p', '我們負責整個探索流程的協調：設計考察行程，讓集團看到的是跨城市的'
                  '可比條件，而不是一趟被安排好的展示；安排政府資源與專業顧問的引薦；'
                  '並彙整這個決策所仰賴的市場與供應鏈研究。'),
            ('p', '我們也負責說實話。如果結論是這個概念需要換一個市場、換一種店型，'
                  '或換一個年份，那我們就把這個結論交出去。'),
            ('h2', '下一階段'),
            ('p', '收斂候選商圈名單、建立可比較的裝修與租金情境試算，並判斷合適的進入時機。'
                  '在那之後，才會開始進行物件談判。'),
            ('panel', '重點整理', '這個專案的關鍵取決於什麼', [
                '這個概念能否在轉換語境後，仍保有它之所以獨特的地方。',
                '二手餐廳空間與毛胚屋的取捨，以及各自對時程與預算的意義。',
                '所選市政區的證照與執照流程順序。',
                '無法在地取得的食材，其供應鏈穩定性。',
                '人力供給，以及遠距經營所需要的管理層厚度。',
                '無營收期實際會有多長。',
            ]),
        ],
    ),
}

# ═══════════════════════════════════════════════════════════════════════════
# PROJECT 02
# ═══════════════════════════════════════════════════════════════════════════
PAGES['taiwan-startup-delegation-arizona'] = {
    'type': 'project', 'hero': 'hero-startup-project.jpg',
    'related': ['arizona-gateway-for-taiwanese-companies', 'first-steps-before-us-expansion'],
    'en': dict(
        category='Technology & Startups', status='Ecosystem Connection · In Progress', statusShort='Ecosystem Connection',
        industry='Technology & Startups', dateLabel='August 2026',
        crumb='Taiwan startup delegation',
        title="Connecting Taiwan Startups with Arizona's Innovation Ecosystem",
        desc='An ongoing programme connecting Taiwanese startup founders with Arizona\'s '
             'innovation ecosystem — university and economic-development engagement, '
             'accelerators, investor introductions and market-entry education.',
        heroAlt='Office towers in downtown Phoenix',
        cardBlurb='Founder exchange, ecosystem engagement and market-entry education, '
                  'currently underway.',
        standfirst='A programme is underway to connect Taiwanese startup founders with '
                   'Arizona\'s innovation ecosystem. It is an introduction and education '
                   'programme — not an investment process, and not a guarantee of any outcome.',
        facts=[('Status', 'Ecosystem Connection · In Progress'),
               ('Industry', 'Technology & Startups'),
               ('Market', 'Greater Phoenix, Arizona'),
               ('Current phase', 'Ecosystem engagement')],
        body=[
            ('h2', 'Background'),
            ('p', 'Taiwanese founders considering the United States often face the same '
                  'problem: the market is legible from a distance, but the ecosystem is not. '
                  'Knowing that a state has universities, accelerators and investors is very '
                  'different from knowing who to talk to, what they respond to, and what a '
                  'realistic first conversation looks like.'),
            ('h2', 'Business objective'),
            ('p', 'To give founders direct, unmediated exposure to the people and institutions '
                  'that make up Arizona\'s innovation ecosystem, so that any subsequent '
                  'decision about entering the market is made from observation rather than '
                  'assumption.'),
            ('h2', 'Market opportunity'),
            ('p', 'Arizona\'s innovation ecosystem is still forming around its advanced '
                  'manufacturing base. For an early-stage company, a forming ecosystem can '
                  'offer more access than a mature one — shorter routes to institutions, more '
                  'willingness to meet, and less competition for attention.'),
            ('pull', 'A forming ecosystem offers more access than a mature one — and less '
             'competition for attention.', None),
            ('fig', 'ind-startup.jpg', 'Mixed-use development in midtown Phoenix',
             'Midtown Phoenix. The ecosystem is being built now, which is why the routes into '
             'it are still short.'),
            ('h2', 'Current progress'),
            ('ul', [
                'Founder exchange sessions between Taiwanese and Arizona-based companies.',
                'Engagement with the Arizona Commerce Authority on state-level resources and '
                'programmes.',
                'Engagement with Arizona State University on research, talent and innovation '
                'programmes.',
                'Visits to incubators and accelerators operating in the metro area.',
                'Introductions to investors and mentors active in the local ecosystem.',
                'Industry-specific connections aligned to each participating company.',
                'Education sessions on the U.S. business environment, entity structures and '
                'market-entry considerations.',
            ]),
            ('advisory', 'This programme provides introductions, information and access. It '
                         'does not include, imply or guarantee investment, government support, '
                         'grant awards, incubator admission or any commercial outcome. Any '
                         'funding, incentive or programme participation is determined solely '
                         'by the relevant organisation on its own terms.'),
            ('h2', "CnC Venture's role"),
            ('p', 'We design and coordinate the programme: identifying which institutions and '
                  'individuals are genuinely relevant to each participating company, arranging '
                  'and preparing the meetings, and providing the context on both sides so the '
                  'conversations start from a useful place.'),
            ('p', 'We also handle the unglamorous part — briefing founders on how a U.S. '
                  'conversation differs from a Taiwanese one, and what a follow-up is actually '
                  'expected to look like.'),
            ('h2', 'Next phase'),
            ('p', 'Continued engagement with the institutions already met, structured follow-up '
                  'for companies with specific interest, and support for those choosing to '
                  'move toward a formal market-entry evaluation.'),
            ('panel', 'Key takeaways', 'What this engagement turns on', [
                'Whether the company\'s customers or partners are actually in this ecosystem, '
                'or elsewhere in the U.S.',
                'What stage the company is at, and whether a U.S. presence is premature.',
                'Which entity structure would suit the company\'s funding and operating plans.',
                'Talent strategy — whether to hire locally, relocate, or operate remotely.',
                'The gap between an introduction and a commercial relationship, and what '
                'closes it.',
            ]),
        ],
    ),
    'zh-tw': dict(
        category='科技與新創', status='生態系連結 · 進行中', statusShort='生態系連結',
        industry='科技與新創', dateLabel='2026 年 8 月',
        crumb='台灣新創代表團',
        title='串聯台灣新創與亞利桑那創新生態系',
        desc='一項進行中的計畫，串聯台灣新創創辦人與亞利桑那創新生態系——'
             '大學與經濟發展單位對接、育成與加速器參訪、投資人引薦，以及市場進入教育。',
        heroAlt='Phoenix 市中心的辦公大樓',
        cardBlurb='創辦人交流、生態系對接與市場進入輔導，目前進行中。',
        standfirst='一項串聯台灣新創創辦人與亞利桑那創新生態系的計畫正在進行。'
                   '它是引薦與教育性質的計畫——不是投資流程，也不對任何結果做出保證。',
        facts=[('狀態', '生態系連結 · 進行中'),
               ('產業', '科技與新創'),
               ('市場', '亞利桑那州・大鳳凰城'),
               ('目前階段', '生態系對接')],
        body=[
            ('h2', '背景'),
            ('p', '考慮進入美國的台灣創辦人，常常遇到同一個問題：市場從遠處看得懂，'
                  '生態系卻看不懂。知道一個州有大學、有加速器、有投資人，'
                  '和知道該找誰談、他們在意什麼、第一次對話合理的樣子是什麼，是兩回事。'),
            ('h2', '事業目標'),
            ('p', '讓創辦人直接、無中介地接觸構成亞利桑那創新生態系的人與機構，'
                  '使後續任何關於進入市場的決定，是建立在觀察之上，而不是假設之上。'),
            ('h2', '市場機會'),
            ('p', '亞利桑那的創新生態系仍圍繞著先進製造基礎持續成形。對早期公司而言，'
                  '一個「正在形成」的生態系，往往比成熟生態系更容易進入——'
                  '接觸機構的路徑更短、對方更願意見面，注意力的競爭也較小。'),
            ('pull', '正在形成的生態系，比成熟的更容易進入——注意力的競爭也比較小。', None),
            ('fig', 'ind-startup.jpg', 'Phoenix 中城的複合式開發街區',
             'Phoenix 中城。這個生態系正在建構中，這也是為什麼進入它的路徑還很短。'),
            ('h2', '目前進度'),
            ('ul', [
                '台灣與亞利桑那在地公司之間的創辦人交流場次。',
                '與 Arizona Commerce Authority 對接，了解州級資源與計畫。',
                '與 Arizona State University 對接研究、人才與創新計畫。',
                '參訪大鳳凰城地區運作中的育成中心與加速器。',
                '引薦在地生態系中活躍的投資人與業師。',
                '依各參與公司的領域，安排產業別的對接。',
                '關於美國營商環境、公司架構與市場進入考量的教育場次。',
            ]),
            ('advisory', '本計畫提供的是引薦、資訊與接觸機會。它不包含、不暗示、'
                         '也不保證投資、政府支持、補助核准、育成錄取或任何商業結果。'
                         '任何資金、優惠或計畫參與資格，均由相關機構依其自身標準單獨決定。'),
            ('h2', 'CnC Venture 的角色'),
            ('p', '我們設計並協調整個計畫：判斷哪些機構與個人對每一家參與公司是真正相關的、'
                  '安排並事前準備會議，並在雙方之間補足脈絡，讓對話從一個有用的位置開始。'),
            ('p', '我們也處理不那麼光鮮的部分——向創辦人說明美式對話與台式對話的差異，'
                  '以及一次「後續聯繫」在對方期待中實際上長什麼樣子。'),
            ('h2', '下一階段'),
            ('p', '與已經接觸的機構持續互動，為具體有意願的公司安排結構化的後續跟進，'
                  '並協助決定要進入正式市場評估的公司往下一步走。'),
            ('panel', '重點整理', '這個專案的關鍵取決於什麼', [
                '公司的客戶或夥伴，實際上是在這個生態系裡，還是在美國其他地方。',
                '公司目前處於什麼階段，設立美國據點是否為時過早。',
                '哪一種公司架構符合公司的募資與營運規劃。',
                '人才策略——在地招募、外派，還是遠距運作。',
                '從「一次引薦」到「一段商業關係」之間的落差，以及什麼能把它補上。',
            ]),
        ],
    ),
}

# ═══════════════════════════════════════════════════════════════════════════
# PROJECT 03
# ═══════════════════════════════════════════════════════════════════════════
PAGES['taiwanese-consumer-brand-us-market-entry'] = {
    'type': 'project', 'hero': 'hero-brand-project.jpg',
    'related': ['first-steps-before-us-expansion', 'phoenix-metro-market-guide'],
    'en': dict(
        category='Consumer & Lifestyle Brands', status='U.S. Market Entry · In Progress', statusShort='U.S. Market Entry',
        industry='Consumer & Lifestyle Brands', dateLabel='August 2026',
        crumb='Consumer brand market entry',
        title='Preparing a Taiwanese Consumer Brand for U.S. Market Entry',
        desc='An ongoing engagement preparing a Taiwanese consumer brand for entry into the '
             'U.S. market — strategy, company setup planning, brand localization, real-estate '
             'evaluation and phased execution.',
        heroAlt='Retail architecture in Old Town Scottsdale',
        cardBlurb='Entry strategy, setup planning and brand localization, currently underway.',
        standfirst='A Taiwanese consumer brand is preparing for entry into the United States. '
                   'The work is preparatory: strategy, structure and localization are being '
                   'developed, and no distribution, retail placement or launch has been '
                   'completed.',
        facts=[('Status', 'U.S. Market Entry · In Progress'),
               ('Industry', 'Consumer & Lifestyle Brands'),
               ('Market', 'United States, Arizona-first'),
               ('Current phase', 'Strategy and preparation')],
        body=[
            ('h2', 'Background'),
            ('p', 'The client has an established consumer brand in Taiwan and is preparing to '
                  'enter the U.S. market. The brand is not named here and will be identified '
                  'publicly only with the client\'s approval.'),
            ('p', 'The starting position is a common one: strong domestic performance, a clear '
                  'product, and an open question about whether the brand story and price '
                  'architecture survive the move to an American customer.'),
            ('h2', 'Business objective'),
            ('p', 'To build a market-entry plan that can be executed in phases — with a defined '
                  'stop point between each — rather than committing to a full launch before '
                  'the market has responded.'),
            ('h2', 'Market opportunity'),
            ('p', 'Arizona offers a launch market that is large enough for results to be '
                  'meaningful but small enough that a first attempt can be adjusted without '
                  'writing off a national rollout. Its metro sub-markets also allow for '
                  'testing across quite different customer profiles within a short drive.'),
            ('pull', 'Large enough for the result to mean something. Small enough that a '
             'first attempt can be adjusted.', None),
            ('fig', 'ind-brand.jpg', 'Retail architecture in Old Town Scottsdale',
             'Old Town Scottsdale. Positioning becomes concrete the moment a street is '
             'chosen.'),
            ('h2', 'Current progress'),
            ('ul', [
                'Market-entry strategy development, including phased scenarios and stop points.',
                'U.S. company setup planning, with structure options under review by '
                'professional advisors.',
                'Brand localization work — positioning, naming considerations, and how the '
                'origin story is told.',
                'Customer and market positioning analysis against comparable brands already in '
                'market.',
                'Packaging and retail considerations, including labelling and compliance '
                'questions.',
                'Commercial real-estate evaluation for potential retail or operational space.',
                'Coordination between legal, accounting and other professional advisors.',
                'Launch planning and phased execution sequencing.',
            ]),
            ('advisory', 'No distribution agreement has been signed, no retail placement '
                         'secured, no lease executed and no launch completed. Labelling, '
                         'compliance and import requirements will be confirmed with qualified '
                         'U.S. professionals before any product enters the market.'),
            ('h2', "CnC Venture's role"),
            ('p', 'We coordinate the preparation across workstreams that would otherwise run '
                  'separately and collide: making sure the entity structure supports the '
                  'distribution model, that the localization decisions are compatible with '
                  'compliance requirements, and that the real-estate evaluation reflects the '
                  'business model rather than the other way round.'),
            ('p', 'We also maintain the phasing discipline — protecting the stop points so that '
                  'each phase has to earn the next.'),
            ('h2', 'Next phase'),
            ('p', 'Finalising the entry structure, completing localization decisions, and '
                  'defining the first-phase launch scope with the criteria that would justify '
                  'proceeding to phase two.'),
            ('panel', 'Key takeaways', 'What this engagement turns on', [
                'Whether the brand story is an asset in the U.S. context or needs reframing.',
                'Price architecture against comparable products already on American shelves.',
                'Labelling, ingredient and claim requirements, which vary by product category.',
                'Whether to enter through direct retail, distribution, or a combination.',
                'The real cost and duration of the pre-revenue period.',
                'What a phase-one result would have to look like to justify phase two.',
            ]),
        ],
    ),
    'zh-tw': dict(
        category='消費與生活品牌', status='市場進入 · 進行中', statusShort='市場進入',
        industry='消費與生活品牌', dateLabel='2026 年 8 月',
        crumb='消費品牌美國市場進入',
        title='協助台灣消費品牌準備進入美國市場',
        desc='一項進行中的合作：協助台灣消費品牌準備進入美國市場——進入策略、公司設立規劃、'
             '品牌在地化、不動產評估與分階段執行。',
        heroAlt='Old Town Scottsdale 的零售建築',
        cardBlurb='進入策略、設立規劃與品牌在地化，目前進行中。',
        standfirst='一個台灣消費品牌正在準備進入美國市場。目前的工作屬於準備階段：'
                   '策略、架構與在地化正在成形，尚未完成任何通路、上架或上市。',
        facts=[('狀態', '市場進入 · 進行中'),
               ('產業', '消費與生活品牌'),
               ('市場', '美國，以亞利桑那為首站'),
               ('目前階段', '策略與準備')],
        body=[
            ('h2', '背景'),
            ('p', '客戶在台灣擁有已具規模的消費品牌，正準備進入美國市場。'
                  '本頁不揭露品牌名稱，只有在客戶同意之後才會對外具名。'),
            ('p', '起點是很常見的一種：國內表現穩健、產品定位清楚，但有一個尚未回答的問題——'
                  '品牌故事與價格架構，在面對美國消費者時是否仍然成立。'),
            ('h2', '事業目標'),
            ('p', '建立一套可以分階段執行的市場進入計畫，且每個階段之間都有明確的停損點；'
                  '而不是在市場還沒有回應之前，就投入完整上市。'),
            ('h2', '市場機會'),
            ('p', '亞利桑那提供的首發市場，規模大到足以讓結果具有意義，'
                  '又小到讓第一次嘗試可以調整，而不必把全國布局一起賠掉。'
                  '這個都會區的次市場，也讓品牌能在短短的車程內測試相當不同的客群樣貌。'),
            ('pull', '大到足以讓結果有意義，小到讓第一次嘗試還能修正。', None),
            ('fig', 'ind-brand.jpg', 'Old Town Scottsdale 的零售建築',
             'Old Town Scottsdale。定位的抉擇，會在選定一條街的那一刻變得具體。'),
            ('h2', '目前進度'),
            ('ul', [
                '市場進入策略建構，包含分階段情境與停損點設計。',
                '美國公司設立規劃，架構選項由專業顧問審視中。',
                '品牌在地化——定位、命名考量，以及品牌來源故事的敘述方式。',
                '對照已在市場上的可比品牌，進行客群與定位分析。',
                '包裝與零售考量，包含標示與法規遵循問題。',
                '評估潛在零售或營運空間的商用不動產。',
                '法律、會計與其他專業顧問之間的協調。',
                '上市規劃與分階段執行順序的設計。',
            ]),
            ('advisory', '尚未簽署任何通路合約、尚未取得零售上架、未執行任何租約，'
                         '也尚未完成上市。標示、法規遵循與進口要求，'
                         '都會在任何產品進入市場之前，與具備資格的美國專業人士確認。'),
            ('h2', 'CnC Venture 的角色'),
            ('p', '我們負責協調那些原本會各自進行、然後互相衝撞的工作線：'
                  '確保公司架構支撐得起通路模式、在地化決策與法規要求彼此相容，'
                  '以及不動產評估是跟著商業模式走，而不是反過來。'),
            ('p', '我們也維持分階段的紀律——守住那些停損點，讓每一個階段都必須'
                  '掙得下一個階段。'),
            ('h2', '下一階段'),
            ('p', '確定進入架構、完成在地化決策，並定義第一階段的上市範圍，'
                  '以及什麼樣的結果才足以支持進入第二階段。'),
            ('panel', '重點整理', '這個專案的關鍵取決於什麼', [
                '品牌故事在美國語境中是資產，還是需要重新框架。',
                '相對於美國貨架上既有的可比產品，價格架構是否站得住。',
                '標示、成分與產品宣稱的要求，會因產品類別而異。',
                '要走直營零售、通路經銷，還是兩者並行。',
                '無營收期實際的成本與長度。',
                '第一階段要跑出什麼樣的結果，才足以支持第二階段。',
            ]),
        ],
    ),
}
