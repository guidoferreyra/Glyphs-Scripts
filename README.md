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
(UI) Backup anchors to a secondary layer and allows to copy them to another layer.

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

#### copyAnchorsFromBase.py
On a suffixed glyph run the script to copy the anchors from the default version. (i.e. run on /a.ss01 and get /a anchors).

---

#### createOTClass.py
(UI) Create an Opentype Class with glyphs containing an specified text.
—This script uses code from Mekkablue's "Make OT class from selected glyphs".

![](readme_imgs/screen-createotclass.png)

---

#### moreThanTwoComponents.py

Based on selected glyphs, opens in a new tab the glyphs that uses more than two components. 

---

#### nodesNearAlignmentZones.py

(UI) Based on a upm “threshold” slider, adds circle annotation to nodes that are close to alignment zones. Useful for misplaced nodes that affects hinting.

![](readme_imgs/screen-nodesNearAlignmentZones.png)

---

#### redCircles.py

Searches for handles that are overlapping nodes and marks them with an annotation circle, setting also the layer label color to orange.

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

