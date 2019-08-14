#(dir, hname, binrange)

histDefs = [
    # ("Digis", "hWireTBin_m11a"),
    ("Digis", "hWireTBin_m11b"),
    ("Digis", "hWireTBin_m12"),
    ("Digis", "hWireTBin_m13"),
    ("Digis", "hWireTBin_m21"),
    ("Digis", "hWireTBin_m22"),
    ("Digis", "hWireTBin_m31"),
    ("Digis", "hWireTBin_m32"),
    ("Digis", "hWireTBin_m41"),
    ("Digis", "hWireTBin_m42"),
    # ("Digis", "hWireTBin_p11a"),
    ("Digis", "hWireTBin_p11b"),
    ("Digis", "hWireTBin_p12"),
    ("Digis", "hWireTBin_p13"),
    ("Digis", "hWireTBin_p21"),
    ("Digis", "hWireTBin_p22"),
    ("Digis", "hWireTBin_p31"),
    ("Digis", "hWireTBin_p32"),
    ("Digis", "hWireTBin_p41"),
    ("Digis", "hWireTBin_p42"),
    ("PedestalNoise", "hStripPedMEm11a"),
    ("PedestalNoise", "hStripPedMEm11b"),
    ("PedestalNoise", "hStripPedMEm12"),
    ("PedestalNoise", "hStripPedMEm13"),
    ("PedestalNoise", "hStripPedMEm21"),
    ("PedestalNoise", "hStripPedMEm22"),
    ("PedestalNoise", "hStripPedMEm31"),
    ("PedestalNoise", "hStripPedMEm32"),
    ("PedestalNoise", "hStripPedMEm41"),
    ("PedestalNoise", "hStripPedMEm42"),
    ("PedestalNoise", "hStripPedMEp11a"),
    ("PedestalNoise", "hStripPedMEp11b"),
    ("PedestalNoise", "hStripPedMEp12"),
    ("PedestalNoise", "hStripPedMEp13"),
    ("PedestalNoise", "hStripPedMEp21"),
    ("PedestalNoise", "hStripPedMEp22"),
    ("PedestalNoise", "hStripPedMEp31"),
    ("PedestalNoise", "hStripPedMEp32"),
    ("PedestalNoise", "hStripPedMEp41"),
    ("PedestalNoise", "hStripPedMEp42"),
    ("recHits", "hRHTimingAnodem11a"),
    ("recHits", "hRHTimingAnodem11b"),
    ("recHits", "hRHTimingAnodem12"),
    ("recHits", "hRHTimingAnodem13"),
    ("recHits", "hRHTimingAnodem21"),
    ("recHits", "hRHTimingAnodem22"),
    ("recHits", "hRHTimingAnodem31"),
    ("recHits", "hRHTimingAnodem32"),
    ("recHits", "hRHTimingAnodem41"),
    ("recHits", "hRHTimingAnodem42"),
    ("recHits", "hRHTimingAnodep11a"),
    ("recHits", "hRHTimingAnodep11b"),
    ("recHits", "hRHTimingAnodep12"),
    ("recHits", "hRHTimingAnodep13"),
    ("recHits", "hRHTimingAnodep21"),
    ("recHits", "hRHTimingAnodep22"),
    ("recHits", "hRHTimingAnodep31"),
    ("recHits", "hRHTimingAnodep32"),
    ("recHits", "hRHTimingAnodep41"),
    ("recHits", "hRHTimingAnodep42"),
    ("Segments", "hSnSegments"),
    ("Segments", "hSnhits"),
    ("recHits", "hRHnrechits"),
    ("recHits", "hRHSumQm11a"),
    ("recHits", "hRHSumQm11b"),
    ("recHits", "hRHSumQm12"),
    ("recHits", "hRHSumQm13"),
    ("recHits", "hRHSumQm21"),
    ("recHits", "hRHSumQm22"),
    ("recHits", "hRHSumQm31"),
    ("recHits", "hRHSumQm32"),
    ("recHits", "hRHSumQm41"),
    ("recHits", "hRHSumQm42"),
    ("recHits", "hRHSumQp11a"),
    ("recHits", "hRHSumQp11b"),
    ("recHits", "hRHSumQp12"),
    ("recHits", "hRHSumQp13"),
    ("recHits", "hRHSumQp21"),
    ("recHits", "hRHSumQp22"),
    ("recHits", "hRHSumQp31"),
    ("recHits", "hRHSumQp32"),
    ("recHits", "hRHSumQp41"),
    ("recHits", "hRHSumQp42"),
    ("recHits", "hRHTimingm11a"),
    ("recHits", "hRHTimingm11b"),
    ("recHits", "hRHTimingm12"),
    ("recHits", "hRHTimingm13"),
    ("recHits", "hRHTimingm21"),
    ("recHits", "hRHTimingm22"),
    ("recHits", "hRHTimingm31"),
    ("recHits", "hRHTimingm32"),
    ("recHits", "hRHTimingm41"),
    ("recHits", "hRHTimingm42"),
    ("recHits", "hRHTimingp11a"),
    ("recHits", "hRHTimingp11b"),
    ("recHits", "hRHTimingp12"),
    ("recHits", "hRHTimingp13"),
    ("recHits", "hRHTimingp21"),
    ("recHits", "hRHTimingp22"),
    ("recHits", "hRHTimingp31"),
    ("recHits", "hRHTimingp32"),
    ("recHits", "hRHTimingp41"),
    ("recHits", "hRHTimingp42"),
    ("recHits", "hRHstposm11a"),
    ("recHits", "hRHstposm11b"),
    ("recHits", "hRHstposm12"),
    ("recHits", "hRHstposm13"),
    ("recHits", "hRHstposm21"),
    ("recHits", "hRHstposm22"),
    ("recHits", "hRHstposm31"),
    ("recHits", "hRHstposm32"),
    ("recHits", "hRHstposm41"),
    ("recHits", "hRHstposm42"),
    ("recHits", "hRHstposp11a"),
    ("recHits", "hRHstposp11b"),
    ("recHits", "hRHstposp12"),
    ("recHits", "hRHstposp13"),
    ("recHits", "hRHstposp21"),
    ("recHits", "hRHstposp22"),
    ("recHits", "hRHstposp31"),
    ("recHits", "hRHstposp32"),
    ("recHits", "hRHstposp41"),
    ("recHits", "hRHstposp42"),
    ("Resolution", "hSResidm11a"),
    ("Resolution", "hSResidm11b"),
    ("Resolution", "hSResidm12"),
    ("Resolution", "hSResidm13"),
    ("Resolution", "hSResidm21"),
    ("Resolution", "hSResidm22"),
    ("Resolution", "hSResidm31"),
    ("Resolution", "hSResidm32"),
    ("Resolution", "hSResidm41"),
    ("Resolution", "hSResidm42"),
    ("Resolution", "hSResidp11a"),
    ("Resolution", "hSResidp11b"),
    ("Resolution", "hSResidp12"),
    ("Resolution", "hSResidp13"),
    ("Resolution", "hSResidp21"),
    ("Resolution", "hSResidp22"),
    ("Resolution", "hSResidp31"),
    ("Resolution", "hSResidp32"),
    ("Resolution", "hSResidp41"),
    ("Resolution", "hSResidp42"),
    ("Segments", "hSGlobalPhi"),
    ("Segments", "hSGlobalTheta"),
    ("Segments", "hSChiSq"),
    ("Segments", "hSTimeCathode"),
    ("Segments", "hSTimeCombined"),
    ("BXMonitor", "hCLCTL1A"),
    ]

