Glyphs-Scripts
==============
Python scripts for the font editor Glyphs App.
Please feel free to report bugs and send suggestions.

#### addAnchorstoGlpyhs.py
Using prebuilt dictionary the script adds anchors to all the master of the selected glyphs.
Feel free to edit the dictionary to match your scheme of anchors.
For those glyphs that are not in the dictionary the script do nothing.
The position of the anchors are estimated, inside the script there is another dictionary with the position of the anchors.

—Thanks to Mark Frömberg (mirque.de) for the angle function.

---

#### anchorBackupAndClone.py
(UI) Backup anchors or copy to another layer.

![](readme_imgs/screen-backupClone.png)


---

#### anchorDictionary.py
Use this complementarty script to create a dictionary based on a previous font.
Outputs to the console.

---

#### centerAnchors.py
Center all anchors of all layers of selected glyphs.

---

#### compareSets.py
(UI) Compares glyph sets between two open fonts and allows to add missing glyph to the other font.

![](readme_imgs/screen-comparesets.png)

---

#### moreThanTwoComponents.py

Based on a selection opens in a newtab the glyphs that uses more than two components. 

---

#### nodesNearAlignmentZones.py

Based on a selection opens in a newtab the glyphs that uses more than two components. 

![](readme_imgs/screen-nodesNearAlignmentZones.png)

---

#### redCircles.py

This script searches for control points that are overlapping nodes and marks them with an annotation circle, setting also the layer label color to orange.

---

#### reportAnchorsnOffMetrics.py

Prints to the console a list with the anchors off the metrics of the selected glyphs.
_This script is a modification of a mekkablue's script._

---

#### reportGlyphAnchors.py

Prints to the console the anchors used on selected Glyphs. 

---

#### slantAnchors.py

(UI) Moves anchors according to master italic angle. Useful when importing anchors from roman versions, or after changing the font angle.

![](readme_imgs/screen-slantAnchors.png)

---

#### smooth2Sharp.py

The script searches smooth nodes with disaligned handles and changes them to sharp. Maybe useful for auto traced illustrations.

