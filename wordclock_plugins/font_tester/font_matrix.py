class font_matrix:
    """
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a german WCA
    """

    def __init__(self):
	

	self.charList = (self.replacement + \
		self.a + \
		self.b + \
		self.c + \
		self.d + \
		self.e + \
		self.f + \
		self.g + \
		self.h + \
		self.i + \
		self.j + \
		self.k + \
		self.l + \
		self.m + \
		self.n + \
		self.o + \
		self.p + \
		self.q + \
		self.r + \
		self.s + \
		self.t + \
		self.u + \
		self.v + \
		self.w + \
		self.x + \
		self.y + \
		self.z)
    def getC(self, currentC):
        return (self.charList[currentC*2] + \
	    self.charList[(currentC*2)+1])

    def getCharCount(self):
	return ((len(self.charList)/2)-1)

	#if no charter is defined, a questionmark will be displayed
    def noChar(self):
	return [range(11,16) + range(22,24) + range(25,27) + [33] + [35] + [37] + range(44,47) + [48] + range(55,57) + range(58,60) + range (66,71) + range(77,79) + range(80,82) + range(88,93), \
	    []]

	#A
    def a(self):
        return [[24] + [34] + [36] + [44] + [48] + range(55,60) + [66] + [70] + [77] + [81] + [88] + [92], \
	    range(62,64) + [72] + [75] + [83] + [86] + range(95,98)]

	self.b=[range(22,26) + [33] + [37] + [44] + [48] + range(55,59) + [66] + [70] + [77] + [81] + range(88,92), \
	    [28] + [39] + [50] + range(61,64) + [72] + [75] + [83] + [86] + range(94,97)]

	self.c=[range(24,27) + [34] + [44] + [55] + [66] + [78] + range(90,93), \
	    range(52,54) + [62] + [73] + [84] + range(96,98)]

	self.d=[range(22,25) + [33] + [36] + [44] + [48] + [55] + [59] + [66] + [70] + [77] + [80] + range(88,91), \
	    [31] + [42] + [53] + range(62,65) + [72] + [75] + [83] + [86] + range(95,98)]

	self.e=[range(22,27) + [33] + [44] + range(55,59) + [66] + [77] + range(88,93), \
	    range(51,53) + [61] + [64] + range(72,76) + [83] + range(95,97)]

	self.f=[range(22,27) + [33] + [44] + range(55,59) + [66] + [77] + [88], \
	    range(30,32) + [40] + [51] + range(61,64) + [73] + [84] + [95]]

	self.g=[range(23,27) + [33] + [44] + [55] + [66] + range(69,71) + [77] + [81] + range(89,93), \
	    range(51,53) + [61] + [64] + [72] + [75] + range(84,87) + [97] + range(106,108)]

	self.h=[[22] + [26] + [33] + [37] + [44] + [48] + range(55,60) + [66] + [70] + [77] + [81] + [88] + [92], \
	    [28] + [39] + [50] + range(61,64) + [72] + [75] + [83] + [86] + [94] + [97]]

	self.i=[range(23,26) + [35] + [46] + [57] + [68] + [79] + range(89,92), \
	    [41] + [63] + [74] + [85] + [96]]

	self.j=[range(24,27) + [36] + [47] + [58] + [69] + [80] + range(89,91), \
	    [64] + [75] + [86] + [97] + [107]]

	self.k=[[22] + [26] + [33] + [36] + [44] + [46] + range(55,57) + [66] + [68] + [77] + [80] + [88] + [92], \
	    [28] + [39] + [50] + [61] + [63] + range(72,74) + [83] + [85] + [94] + [96]]

	self.l=[[22] + [33] + [44] + [55] + [66] + [77] + range(88,92), \
	    [28] + [39] + [50] + [61] + [72] + [83] + range(95,96)]

	self.m=[[22] + [26] + range(33,35) + range(36,38) + [44] + [46] + [48] + [55] + [59] + [66] + [70] + [77] + [81] + [88] + [92], \
	    range(61,66) + [72] + [74] + [76] + [83] + [85] + [87] + [94] + [96] + [98]]

	self.n=[[22] + [26] + [33] + [37] + range(44,46) + [48] + [55] + [57] + [59] + [66] + range(69,71) + [77] + [81] + [88] + [92], \
	    range(61,64) + [72] + [74] + [83] + [85] + [94] + [96]]

	self.o=[range(22,27) + [33] + [37] + [44] + [48] + [55] + [59] + [66] + [70] + [77] + [81] + range(88,93), \
	    range(61,65) + [72] + [75] + [83] + [86] + range(94,98)]

	self.p=[range(22,25) + [33] + [36] + [44] + [47] + range(55,58) + [66] + [77] + [88], \
	    range(51,53) + [61] + [64] + [72] + [75] + range(83,86) + [94] + [105]]

	self.q=[range(22,27) + [33] + [37] + [44] + [48] + [55] + [59] + [66] + [68] + [70] + [77] + range(80,82) + range(88,92), \
	    range(52,54) + [62] + [65] + [73] + [76] + range(85,88) + [98] + [109]]

	self.r=[range(22,25) + [33] + [36] + [44] + [47] + range(55,58) + [66] + [69] + [77] + [80] + [88] + [91], \
	    range(61,64) + [72] + [83] + [94]]

	self.s=[range(23,26) + [33] + [44] + range(56,58) + [69] + [80] + range(88,91), \
	    range(52,54) + [62] + [74] + [86] + range(95,97)]

	self.t=[range(22,27) + [35] + [46] + [57] + [68] + [79] + [90], \
	    [30] + range(40,43) + [52] + [63] + [74] + [85] + range(96,98)]

	self.u=[[22] + [26] + [33] + [37] + [44] + [48] + [55] + [59] + [66] + [70] + [77] + [81] + range(89,92), \
	    [61] + [64] + [72] + [75] + [83] + [86] + range(95,97)]

	self.v=[[22] + [26] + [33] + [37] + [44] + [48] + [55] + [59] + [66] + [70] + [78] + [80] + [90], \
	    [62] + [64] + [73] + [75] + [84] + [86] + [96]]

	self.w=[[22] + [26] + [33] + [37] + [44] + [48] + [55] + [59] + [66] + [68] + [70] + [77] + [79] + [81] + [89] + [91], \
	    [61] + [65] + [72] + [76] + [83] + [85] + [87] + [95] + [97]]

	self.x=[[22] + [26] + [33] + [37] + [45] + [47] + [57] + [67] + [69] + [77] + [81] + [88] + [92], \
	    [72] + [74] + [84] + [94] + [96]]

	self.y=[[22] + [26] + [33] + [37] + range(45,48) + [57] + [68] + [79] + [90], \
	    [62] + [64] + [73] + [75] + range(85,87) + [97] + [108]]

	self.z=[range(22,27) + [37] + [47] + [57] + [67] + [77] + range(88,93), \
	    range(62,66) + [75] + [85] + range(95,99)]