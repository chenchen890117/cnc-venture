# -*- coding: utf-8 -*-
"""Traditional Chinese copy for CnC Venture.

This is not a translation of the English page. It is the same brand speaking
to a different reader: a Taiwanese owner or executive weighing up the United
States. Where a literal rendering would sound like a translated American
website, the sentence has been rewritten from scratch.

Conventions:
  · U.S. city names stay in Latin script (Phoenix, Scottsdale, Tempe…).
    Taiwanese business writing refers to them that way; inventing
    transliterations for Tempe or Gilbert would read as amateurish.
    「大鳳凰城」 is used for the metro area, where the Chinese term is standard.
  · Em dashes are 「——」, not 「-」. Enumeration uses 「、」.
  · No 「我們致力於」, no 「一站式」, no government-report register.
"""

# (source substring in the English DOM, replacement) — order matters.
REPLACEMENTS = [

    # ── chrome ────────────────────────────────────────────────────────────
    ('>Skip to content<', '>跳至主要內容<'),
    ('>About<', '>關於<'),
    ('>Services<', '>服務<'),
    ('>Industries<', '>產業<'),
    ('>Expansion Stories<', '>專案<'),
    ('>Insights<', '>觀點<'),
    ('>Arizona<', '>亞利桑那<'),
    ('>Contact<', '>聯絡<'),
    ('>Start Your Expansion <', '>開始拓展 <'),
    ('aria-label="Primary"', 'aria-label="主要導覽"'),
    ('aria-label="Mobile"', 'aria-label="行動版導覽"'),
    ('aria-label="Language"', 'aria-label="語言"'),
    ('aria-label="Open menu"', 'aria-label="開啟選單"'),
    ('aria-label="Close menu"', 'aria-label="關閉選單"'),
    ('data-label-open="Open menu" data-label-close="Close menu"',
     'data-label-open="開啟選單" data-label-close="關閉選單"'),

    # ── 1 · hero ──────────────────────────────────────────────────────────
    ('>Business Expansion Platform · Taiwan → United States<',
     '>企業海外拓展平台 · 台灣 → 美國<'),
    # EXPAND stays in Latin: it is the brand gesture, not a word to translate.
    ('>Beyond Borders.<', '>讓世界，看見你的下一步。<'),
    ('>Helping ambitious companies launch, build, and grow in the United States.<',
     '>從市場探索、公司設立到品牌落地，陪伴企業在美國建立下一個成長據點。<'),
    ('>Start Your U.S. Expansion <', '>開始美國市場拓展 <'),
    ('>Explore Arizona<', '>探索亞利桑那<'),
    ('> Scroll<', '> 向下探索<'),

    # ── 2 · why arizona ───────────────────────────────────────────────────
    ('>01 — Why Arizona<', '>01 — 為什麼是亞利桑那<'),
    ('>The desert is where<br>America is building next.<',
     '>美國的下一段建設，<br>正在沙漠裡展開。<'),
    ('>Arizona has emerged as one of the most dynamic gateways for companies '
     'entering the U.S. market. Its growing semiconductor and advanced '
     'manufacturing ecosystem, business-friendly environment, expanding '
     'population, and strong public-private partnerships create meaningful '
     'opportunities for international businesses.<',
     '>亞利桑那已成為國際企業進入美國市場最具動能的門戶之一。半導體與先進製造聚落持續擴張、'
     '營商環境友善、人口穩定成長，加上政府與民間之間長期而具體的協作，為國際企業創造了'
     '真正可行的機會。<'),
    ('>For companies arriving from Taiwan, Arizona offers access to a growing '
     'market, an established Taiwanese business community, and local partners '
     'who understand the realities of cross-border expansion.<',
     '>對來自台灣的企業而言，這裡的意義更為具體：一個仍在成長的市場、一個已經成形的台商社群，'
     '以及真正理解跨境經營現實的在地夥伴。<'),
    ('>CnC Venture helps companies evaluate these opportunities firsthand '
     'through market research, site visits, government and industry '
     'introductions, professional advisory resources, and practical local '
     'execution.<',
     '>CnC Venture 協助企業親自驗證這些機會——透過市場調研、實地考察、政府與產業引薦、'
     '專業顧問資源，以及真正落地的執行支援。<'),
    ('>Read the city guide <', '>閱讀城市指南 <'),
    ('>Downtown Phoenix at street level.<', '>Phoenix 市中心街景。<'),

    ('>Advanced<br>Manufacturing<', '>先進製造<'),
    ('>A rapidly growing semiconductor and technology supply-chain ecosystem.<',
     '>持續擴張的半導體與科技供應鏈聚落。<'),
    ('>Greater<br>Phoenix<', '>大鳳凰城<'),
    ('>One of the largest and fastest-growing metropolitan markets in the '
     'western United States.<',
     '>美國西部規模最大、成長最快的都會市場之一。<'),
    ('>Business<br>Environment<', '>營商環境<'),
    ('>Competitive operating conditions and active economic development support.<',
     '>具競爭力的營運條件，以及積極的經濟發展支持。<'),
    ('>Taiwan–Arizona<br>Connections<', '>台灣—亞利桑那<br>商業連結<'),
    ('>A growing network of Taiwanese businesses, suppliers, professionals, '
     'and public-sector partners.<',
     '>逐步成形的台商、供應商、專業人士與公部門網絡。<'),
    ('>Verified market data and official sources will be added before launch.<',
     '>經查證的市場數據與官方來源，將於正式上線前補齊。<'),

    # ── 3 · journey ───────────────────────────────────────────────────────
    ('>02 — Your Expansion Journey<', '>02 — 拓展歷程<'),
    ('>Expansion is not an event.<br>It is a sequence.<',
     '>拓展不是一個決定，<br>而是一連串的步驟。<'),
    ('>Each step earns the next. We work through all five with you — and we '
     'are still there for the fifth.<',
     '>每一步都為下一步鋪路。這五個階段我們全程參與——包括最後那一段。<'),
    ('>Market Discovery<', '>市場探索<'),
    ('>Market research, business visits, local introductions, customer '
     'validation, and opportunity assessment.<',
     '>市場調研、企業拜訪、在地引薦、客戶驗證與機會評估。<'),
    ('>U.S. Strategy &amp; Setup<', '>美國策略與設立<'),
    ('>Market-entry strategy, company formation, legal and accounting '
     'coordination, and brand localization.<',
     '>進入市場策略、公司設立、法律與會計協調，以及品牌在地化。<'),
    ('>Site Selection &amp; Local Resources<', '>選址與在地資源<'),
    ('>Commercial real estate, location assessment, lease coordination, '
     'government resources, and professional partners.<',
     '>商用不動產、地點評估、租約協商、政府資源與專業夥伴。<'),
    ('>Market Entry Execution<', '>落地執行<'),
    ('>Permits, design, construction, supply chain, hiring, launch '
     'preparation, and local partnerships.<',
     '>證照、設計、施工、供應鏈、人才招募、開幕籌備與在地合作。<'),
    ('>Operations &amp; Growth<', '>營運與成長<'),
    ('>Ongoing operations, marketing, expansion, investment connections, and '
     'long-term growth support.<',
     '>日常營運、行銷、展店、投資對接與長期成長支持。<'),

    # ── 4 · industries ────────────────────────────────────────────────────
    ('>03 — Industries<', '>03 — 產業<'),
    ('>Five ways into<br>the American market.<', '>進入美國市場的<br>五種路徑。<'),
    ('>Food &amp; Beverage<', '>餐飲品牌<'),
    ('>Site selection, permits, kitchen planning, supply chain, local '
     'operations, and brand adaptation.<',
     '>選址、證照、廚房規劃、供應鏈、在地營運與品牌調整。<'),
    ('>Consumer &amp; Lifestyle Brands<', '>消費與生活品牌<'),
    ('>Market positioning, distribution, packaging, retail strategy, and U.S. '
     'brand localization.<',
     '>市場定位、通路布局、包裝設計、零售策略與美國品牌在地化。<'),
    ('>Retail &amp; Franchise<', '>零售與加盟<'),
    ('>Trade-area analysis, location strategy, franchise preparation, leasing, '
     'and store execution.<',
     '>商圈分析、據點策略、加盟制度準備、租賃與門市執行。<'),
    ('>Technology &amp; Startups<', '>科技與新創<'),
    ('>Company setup, ecosystem connections, investors, accelerators, '
     'university resources, and business development.<',
     '>公司設立、生態系連結、投資人與加速器對接、大學資源與商務開發。<'),
    ('>Manufacturing &amp; Industrial Services<', '>製造與工業服務<'),
    ('>Industrial sites, customer proximity, supply-chain coordination, '
     'permits, workforce, and local government support.<',
     '>廠址評估、鄰近客戶布局、供應鏈協調、證照、人力與地方政府支持。<'),

    # ── 5 · expansion in progress ─────────────────────────────────────────
    ('>04 — Expansion in Progress<', '>04 — 進行中的專案<'),
    ('>Work currently underway,<br>reported as it stands.<',
     '>正在進行的工作，<br>如實呈現。<'),
    ('>These are live engagements, not finished case studies. We will publish '
     'outcomes when there are outcomes to publish.<',
     '>這些是進行中的合作，不是完成的案例。有成果的時候，我們再談成果。<'),
    ('>Market Exploration · In Progress<', '>市場探索 · 進行中<'),
    ('>Taiwanese Restaurant Group Exploring Phoenix<',
     '>台灣餐飲集團・Phoenix 市場探索<'),
    ('>Market visits, site selection, government meetings, professional '
     'advisory coordination, and supply-chain assessment.<',
     '>實地考察、選址評估、政府會議、專業顧問協調與供應鏈評估。<'),
    ('>Ecosystem Connection · In Progress<', '>生態系連結 · 進行中<'),
    ('>Taiwan Startup Delegation to Arizona<', '>台灣新創代表團・亞利桑那<'),
    ('>Founder exchange, investor introductions, ACA and ASU engagement, '
     'innovation ecosystem visits, and market-entry education.<',
     '>創辦人交流、投資人引薦、ACA 與 ASU 對接、創新生態系參訪與市場進入輔導。<'),
    ('>U.S. Market Entry · In Progress<', '>市場進入 · 進行中<'),
    ('>Taiwanese Companies Preparing for U.S. Market Entry<',
     '>台灣企業・美國市場進入準備<'),
    ('>Company formation planning, brand localization, professional resource '
     'coordination, real estate evaluation, and execution strategy.<',
     '>公司設立規劃、品牌在地化、專業資源協調、不動產評估與執行策略。<'),
    ('>Multiple sectors<', '>跨產業<'),
    ('>Explore Current Projects <', '>了解進行中的專案 <'),

    # ── 6 · insights ──────────────────────────────────────────────────────
    ('>05 — Insights<', '>05 — 觀點<'),
    ('>The Expansion Journal<', '>拓展誌<'),
    ('>A business magazine on building in America — market reports, city '
     'guides, and the numbers behind the decisions.<',
     '>一本關於「在美國落地」的商業誌——市場觀察、城市指南，以及每個決定背後的真實考量。<'),
    ('>Market Overview<', '>市場觀察<'),
    ('>Coming Soon<', '>即將推出<'),
    ('>Why Arizona Is Becoming a Strategic Gateway for Taiwanese Companies<',
     '>為什麼亞利桑那，正成為台灣企業進軍美國的重要起點？<'),
    ('>An introduction to Arizona\'s business ecosystem, major industries, '
     'Taiwanese connections, and the opportunities companies should evaluate '
     'before entering the market.<',
     '>從產業結構、重點聚落、台灣連結到實際機會，帶你看懂進入這個市場之前，應該先理解的事。<'),
    ('>Read the overview <', '>閱讀全文 <'),
    ('>City Guide<', '>城市指南<'),
    ('>Phoenix Metro Market Guide: Choosing the Right City<',
     '>大鳳凰城市場指南：如何選擇你的第一個城市<'),
    ('>Phoenix, Scottsdale, Tempe, Mesa, Gilbert, and Chandler serve different '
     'customers, industries, and business models.<',
     '>Phoenix、Scottsdale、Tempe、Mesa、Gilbert 與 Chandler，服務的客群、產業與商業模式各不相同。<'),
    ('>Industry Guide<', '>產業指南<'),
    ('>What Taiwanese Restaurant Brands Should Know Before Entering the U.S.<',
     '>台灣餐飲品牌前進美國前，該先知道的事<'),
    ('>Key considerations including market positioning, location, permits, '
     'construction, supply chain, staffing, and local consumer expectations.<',
     '>市場定位、選址、證照、施工、供應鏈、人力，以及美國消費者的實際期待。<'),
    ('>Practical Guide<', '>實務指南<'),
    ('>The First Steps to Establishing a Business in Arizona<',
     '>前進美國市場前，你需要先準備什麼？<'),
    ('>A practical overview of company setup, professional advisors, market '
     'validation, location strategy, and launch planning.<',
     '>公司設立、專業顧問、市場驗證、據點策略與開業規劃的完整概覽。<'),

    # ── 7 · city guide ────────────────────────────────────────────────────
    ('>06 — Arizona City Guide<', '>06 — 亞利桑那城市指南<'),
    ('>One valley.<br>Six very different answers.<',
     '>一個谷地，<br>六種不同的答案。<'),
    ('>Greater Phoenix is not a single market. Each city serves different '
     'customers, industries, and business models — and the right address '
     'depends on which of them you need.<',
     '>大鳳凰城不是單一市場。每座城市服務的客群、產業與商業模式都不同——該落在哪裡，'
     '取決於你需要什麼。<'),
    ('>The centre of gravity<', '>重心所在<'),
    ('>Government, business services, major commercial districts, and access '
     'to the broader metro market.<',
     '>政府機關、商業服務、主要商業區，以及通往整個都會區的樞紐。<'),
    ('>Where the market pays a premium<', '>願意付出溢價的市場<'),
    ('>Premium hospitality, dining, tourism, lifestyle retail, and affluent '
     'customers.<',
     '>高端接待、餐飲、觀光、生活風格零售與高消費客群。<'),
    ('>The talent<', '>人才所在<'),
    ('>ASU, startups, innovation, young professionals, and technology-oriented '
     'businesses.<',
     '>ASU、新創、創新能量、年輕專業人口與科技導向企業。<'),
    ('>Room to build<', '>還有空間可以蓋<'),
    ('>Industrial growth, logistics, aerospace, land availability, and '
     'expanding residential communities.<',
     '>工業成長、物流、航太、土地供給與持續擴張的住宅社區。<'),
    ('>The family market<', '>家庭市場<'),
    ('>Family-oriented communities, strong household demographics, retail, and '
     'dining opportunities.<',
     '>家庭型社區、穩健的家戶結構，以及零售與餐飲機會。<'),
    ('>The technology corridor<', '>科技廊帶<'),
    ('>Semiconductors, technology, advanced manufacturing, corporate offices, '
     'and international supply chains.<',
     '>半導體、科技、先進製造、企業辦公室與國際供應鏈。<'),

    # ── 8 · partners ──────────────────────────────────────────────────────
    ('>07 — Partners<', '>07 — 合作生態系<'),
    ('>An ecosystem,<br>not a logo wall.<', '>是生態系，<br>不是 logo 牆。<'),
    ('>Expansion depends on the quality of the people around it. These are the '
     'eight relationships we help companies build during their first year in '
     'the United States.<',
     '>拓展的成敗，很大程度取決於身邊的人。這八種關係，會陪企業走過在美國的第一年。<'),
    ('>Government<', '>政府單位<'),
    ('>Economic development teams and public-sector resources that help '
     'companies understand local requirements and opportunities.<',
     '>經濟發展團隊與公部門資源，協助企業理解在地法規要求與可用機會。<'),
    ('>CPA<', '>會計師<'),
    ('>U.S. entity structure, sales tax, transfer pricing, and first-year '
     'accounting set up correctly from the start.<',
     '>美國公司架構、銷售稅、移轉訂價，以及第一年就做對的帳務基礎。<'),
    ('>Attorney<', '>律師<'),
    ('>Corporate, employment, and intellectual property counsel for the '
     'agreements signed early in a market you are still learning.<',
     '>公司、勞動與智慧財產法務——處理你還在熟悉市場時，就得簽下的那些合約。<'),
    ('>Commercial Real Estate<', '>商用不動產<'),
    ('>Tenant-side brokers who represent your interests in site search, lease '
     'terms, and negotiation.<',
     '>代表承租方立場的經紀人，協助選址、租約條件與談判。<'),
    ('>Construction<', '>營造工程<'),
    ('>General contractors, architects, and design teams experienced with '
     'comparable build-outs in the local market.<',
     '>具備同類型工程經驗的總承包商、建築師與設計團隊。<'),
    ('>Supply Chain<', '>供應鏈<'),
    ('>Freight, 3PL, customs brokerage, and suppliers already operating within '
     'the Arizona corridor.<',
     '>貨運、第三方物流、報關，以及已在亞利桑那走廊營運的供應商。<'),
    ('>Universities<', '>大學資源<'),
    ('>ASU and the University of Arizona — research collaboration, talent '
     'pipelines, and innovation programmes.<',
     '>ASU 與亞利桑那大學——研究合作、人才管道與創新計畫。<'),
    ('>Investors<', '>投資人<'),
    ('>Angels, family offices, and funds with experience evaluating '
     'cross-border businesses.<',
     '>具備跨境企業評估經驗的天使投資人、家族辦公室與基金。<'),

    # ── 9 · closing cta ───────────────────────────────────────────────────
    ('>Book a strategy session<', '>預約策略諮詢<'),
    ('>Ready to Build Your Next Chapter?<', '>準備好，寫下你的下一章了嗎？<'),
    ('>Start with a focused conversation about your company, expansion goals, '
     'timeline, and the U.S. market opportunities you are considering. We will '
     'help you identify the most practical next step.<',
     '>先從一場聚焦的對話開始——談你的公司、拓展目標、時程，以及你正在評估的美國市場機會。'
     '我們會協助你找出最務實的下一步。<'),
    ('>Book a Strategy Session <', '>預約策略諮詢 <'),

    # ── footer ────────────────────────────────────────────────────────────
    ('>Expand Beyond Borders.<', '>讓世界，看見你的下一步。<'),
    ('>Platform<', '>平台<'),
    ('>Expansion Journey<', '>拓展歷程<'),
    ('>Partner Ecosystem<', '>合作生態系<'),
    ('>Journal<', '>拓展誌<'),
    ('>Arizona City Guide<', '>亞利桑那城市指南<'),
    ('>Expansion in Progress<', '>進行中的專案<'),
    ('>Why Arizona<', '>為什麼是亞利桑那<'),
    ('>Taipei, Taiwan<', '>台北，台灣<'),
    ('>© 2026 CnC Venture. A business expansion platform.<',
     '>© 2026 CnC Venture. 企業海外拓展平台。<'),
    ('>Taiwan → United States<', '>台灣 → 美國<'),
]

# Image descriptions for screen readers.
ALT_TEXT = {
    'Greater Phoenix at dusk, seen from the surrounding mountains': '黃昏時分，自環繞的山區俯瞰大鳳凰城',
    'Light rail and pedestrians on a street in downtown Phoenix': 'Phoenix 市中心街道上的輕軌與行人',
    'Restaurant patio and pool at dusk in the Phoenix area': '鳳凰城地區餐廳庭院與泳池的黃昏景象',
    'Retail architecture in Old Town Scottsdale': 'Old Town Scottsdale 的零售建築',
    'Downtown Gilbert, Arizona, at dusk': '黃昏時分的 Gilbert 市中心',
    'Mixed-use development in midtown Phoenix': 'Phoenix 中城的複合式開發街區',
    'Manufacturing and industrial services expansion': '製造與工業服務',
    'Street scene in central Phoenix': 'Phoenix 市中心街景',
    'Office towers in downtown Phoenix': 'Phoenix 市中心的辦公大樓',
    'Desert park and buttes in the Phoenix metro area': '大鳳凰城地區的沙漠公園與岩丘',
    'The Phoenix valley at dusk': '黃昏時分的鳳凰城谷地',
    'A Phoenix neighbourhood with desert planting': '種滿沙漠植栽的鳳凰城社區',
    'Resort pools at dusk in Scottsdale': '黃昏時分 Scottsdale 的度假泳池',
    'Visitors beside water in an Arizona desert garden': '亞利桑那沙漠花園中的水岸與訪客',
    'Downtown Phoenix, Arizona': 'Phoenix 市中心',
    'Scottsdale, Arizona': '亞利桑那州 Scottsdale',
    'Tempe, Arizona': '亞利桑那州 Tempe',
    'Mesa, Arizona': '亞利桑那州 Mesa',
    'Gilbert, Arizona': '亞利桑那州 Gilbert',
    'Chandler, Arizona': '亞利桑那州 Chandler',
    'Golden light across a saguaro hillside in Arizona': '金色光線灑落亞利桑那的巨柱仙人掌山坡',
}
