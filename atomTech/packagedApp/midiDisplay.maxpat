{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 1,
			"revision" : 3,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 0.0, 0.0, 640.0, 480.0 ],
		"bglocked" : 0,
		"openinpresentation" : 0,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 1,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 1,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 1,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-44",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 1020.0, 330.0, 67.0, 22.0 ],
					"save" : [ "#N", "thispatcher", ";", "#Q", "end", ";" ],
					"text" : "thispatcher"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-43",
					"maxclass" : "toggle",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 1020.0, 225.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1020.0, 285.0, 85.0, 22.0 ],
					"text" : "presentation 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 1020.0, 150.0, 60.0, 22.0 ],
					"text" : "loadmess"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 465.0, 90.0, 58.0, 22.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Apple Color Emoji",
					"fontsize" : 48.0,
					"id" : "obj-36",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 390.0, 394.0, 742.0, 69.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 450.0, 30.0, 577.0, 69.0 ],
					"text" : "A.T.O.M. Controller",
					"textcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.898039215686275, 0.070588235294118, 0.152941176470588, 1.0 ],
					"id" : "obj-37",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 105.0, 165.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 407.0, 10.25, 632.5, 108.5 ],
					"proportion" : 0.5,
					"rounded" : 51
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Apple Color Emoji",
					"fontsize" : 48.0,
					"id" : "obj-32",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 365.25, 360.0, 742.0, 69.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 135.0, 610.75, 269.0, 69.0 ],
					"text" : "Velocity:",
					"textcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"id" : "obj-33",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 120.0, 180.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 105.0, 587.25, 315.0, 122.5 ],
					"proportion" : 0.5,
					"rounded" : 56
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Apple Color Emoji",
					"fontsize" : 48.0,
					"id" : "obj-31",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 372.0, 375.0, 742.0, 69.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 165.0, 302.0, 153.0, 69.0 ],
					"text" : "Note:",
					"textcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ]
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"id" : "obj-29",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 125.0, 161.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 135.0, 277.5, 210.0, 123.5 ],
					"proportion" : 0.5,
					"rounded" : 76
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"horizontal_direction" : 1,
					"id" : "obj-22",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 120.0, 161.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 526.75, 543.25, 240.0, 4.0 ],
					"proportion" : 0.5,
					"rounded" : 46,
					"vertical_direction" : 2
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"horizontal_direction" : 1,
					"id" : "obj-23",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 105.0, 180.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 676.75, 771.25, 240.0, 4.0 ],
					"proportion" : 0.5,
					"rounded" : 46,
					"vertical_direction" : 2
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"horizontal_direction" : 1,
					"id" : "obj-24",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 75.0, 165.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 781.75, 543.25, 128.0, 128.0 ],
					"proportion" : 0.5,
					"shape" : 2,
					"vertical_direction" : 2
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"id" : "obj-25",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 135.0, 143.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 526.75, 647.25, 128.0, 128.0 ],
					"proportion" : 0.5,
					"shape" : 2
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.898039215686275, 0.070588235294118, 0.152941176470588, 1.0 ],
					"fontname" : "Apple Color Emoji",
					"fontsize" : 72.0,
					"id" : "obj-27",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 360.0, 360.0, 424.0, 103.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 609.75, 610.75, 218.0, 103.0 ],
					"textcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
					"triangle" : 0
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"horizontal_direction" : 1,
					"id" : "obj-21",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 125.0, 165.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 530.25, 225.0, 240.0, 4.0 ],
					"proportion" : 0.5,
					"rounded" : 46,
					"vertical_direction" : 2
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"horizontal_direction" : 1,
					"id" : "obj-20",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 90.0, 165.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 680.25, 453.0, 240.0, 4.0 ],
					"proportion" : 0.5,
					"rounded" : 46,
					"vertical_direction" : 2
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"horizontal_direction" : 1,
					"id" : "obj-18",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 105.0, 180.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 785.25, 225.0, 128.0, 128.0 ],
					"proportion" : 0.5,
					"shape" : 2,
					"vertical_direction" : 2
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"id" : "obj-17",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 120.0, 143.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 530.25, 329.0, 128.0, 128.0 ],
					"proportion" : 0.5,
					"shape" : 2
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.898039215686275, 0.070588235294118, 0.152941176470588, 1.0 ],
					"fontname" : "Apple Color Emoji",
					"fontsize" : 72.0,
					"format" : 4,
					"id" : "obj-26",
					"maxclass" : "number",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "bang" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 365.25, 358.650003880262375, 424.0, 103.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 635.25, 285.0, 167.0, 103.0 ],
					"textcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
					"triangle" : 0
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "int", "int" ],
					"patching_rect" : [ 372.0, 284.0, 59.0, 22.0 ],
					"text" : "unpack i i"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-7",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 8,
					"outlettype" : [ "", "", "", "int", "int", "", "int", "" ],
					"patching_rect" : [ 365.0, 249.0, 92.5, 22.0 ],
					"text" : "midiparse"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "int" ],
					"patching_rect" : [ 360.0, 212.0, 40.0, 22.0 ],
					"text" : "midiin"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 413.0, 322.0, 32.0, 22.0 ],
					"text" : "print"
				}

			}
, 			{
				"box" : 				{
					"applycolors" : 1,
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"bgfillcolor_angle" : 270.0,
					"bgfillcolor_autogradient" : 0.0,
					"bgfillcolor_color" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"bgfillcolor_color1" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
					"bgfillcolor_color2" : [ 0.2, 0.2, 0.2, 1.0 ],
					"bgfillcolor_proportion" : 0.5,
					"bgfillcolor_type" : "color",
					"color" : [ 0.898039215686275, 0.070588235294118, 0.152941176470588, 1.0 ],
					"elementcolor" : [ 0.898039215686275, 0.070588235294118, 0.152941176470588, 1.0 ],
					"id" : "obj-4",
					"items" : [ "AU DLS Synth 1", ",", "IAC Driver Bus 1", ",", "from Max 1", ",", "from Max 2" ],
					"maxclass" : "umenu",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "int", "", "" ],
					"parameter_enable" : 0,
					"patching_rect" : [ 360.0, 161.0, 100.0, 22.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 646.75, 150.0, 158.0, 22.0 ],
					"textcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
					"truncate" : 2,
					"underline" : 1
				}

			}
, 			{
				"box" : 				{
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"blinkcolor" : [ 0.607843137254902, 0.325490196078431, 0.909803921568627, 1.0 ],
					"id" : "obj-3",
					"maxclass" : "button",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"outlinecolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
					"parameter_enable" : 0,
					"patching_rect" : [ 360.0, 63.0, 24.0, 24.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 706.75, 174.0, 24.0, 24.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 360.0, 117.0, 50.0, 22.0 ],
					"text" : "midiinfo"
				}

			}
, 			{
				"box" : 				{
					"angle" : 270.0,
					"bgcolor" : [ 0.968627450980392, 0.729411764705882, 0.074509803921569, 1.0 ],
					"id" : "obj-35",
					"maxclass" : "panel",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 125.0, 165.0, 128.0, 128.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 631.75, 135.0, 183.0, 67.25 ],
					"proportion" : 0.5
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-3", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-43", 0 ],
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-44", 0 ],
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-41", 0 ],
					"source" : [ "obj-43", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-6", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-26", 0 ],
					"order" : 1,
					"source" : [ "obj-9", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-27", 0 ],
					"source" : [ "obj-9", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"order" : 0,
					"source" : [ "obj-9", 0 ]
				}

			}
 ],
		"dependency_cache" : [  ],
		"autosave" : 0,
		"bgcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
		"editing_bgcolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ],
		"stripecolor" : [ 0.576470588235294, 0.533333333333333, 0.533333333333333, 1.0 ]
	}

}
