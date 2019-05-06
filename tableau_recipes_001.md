recipe "dashboard":

- open Tableau
- click on the left hand nav bar "Sample-Superstore"

- rename sheet1 to "sales distr. by region"
- hold down CTRL and click on both "Region" and "Sales" to select/highlight them, then on "Show Me" in the upper right
- then click on the pie chart icon
- change top bar drop-down from "standard" to "entire view"
- click on "Show Me" again to reveal the legend

- click on "New Worksheet"
- select "Sales" & "State", click "Show Me", choose "Symbol Maps"
- drag "Region" pill to color
- click on "size" button in "Marks" card to adjust size of marks

- make another worksheet "Sales Distr. by Region & Category"
- drag Region pill to Columns cell
- drag Category (under product) to rows
- grab Sales from measures to columns

=================================

- click on "new dashboard"
- click under size, from fixed size to automatic
- drag first sheet (sales distr. by region) onto the blank "drop sheets here" dashboard space
- then grab the next sheet (the map), drag and drop it to the right of the first (pie) chart
- then grab the last sheet (the bar chart), drag and drop under the pie chart (to take up 1/4 of the dashboard)
- notice that the last dropped section is selected (see the gray border)
- change "standard" to "entire view" for just the currently selected sheet graph
- click in a section/pane to select it, then use the gray tab at the top to drag it elsewhere, such as to take up 1/4 of the screen to the right of the pie chart
- in the lower left corner of the screen (above where it says data source) click on "show dashboard title, Dashboard 1 will appear at the top of the panes/windows, double click to rename "Sales Distr. Dashboard". Keep in mind that the dashboard name is distinct & separate from the title
- To display an image, drag from the "Objects" card the word/pill "Image" to your Dashboard panes/windows. An import prompt will come up to allow you to pick an image.
- After you have imported an image, click on the down caret underneath the "X" delete icon, to select "fit image"
- You may also make the image "float" in the same manner as setting "fit image" by instead choosing "floating"

- now, we'd like interactivity to propagate through the entire dashboard

- oops, go back to filter on "sales distr. by region & cat." by "order date", choose years in popup, choose all years, then OK
- next, under the "Filters" card, click on the YEAR(order date) pill dropdown, and select "Show filter"
- now, back in the dashboard, select the "sales distr. by region & cat.", from the dropdown caret select "filters" and "year of order date"

- then, click on the newest filter card titled "year of order date" to the far right, then on its dropdown, choose "selected worksheets" and then press the button "all on dashboard" on the bottom left of the popup

- pro-tip: you can fix any graph or map using the "pushpin" icon

"filter actions"
- on sales dashboard icon, right mouse click and duplicate it, rename to "Filter Action"
- at top toolbar, click dashboard > actions
- click "add action" then "filter"
- rename to "Region Filter", make sure only "Sales Distr. by Region" is selected at the top, and the other 2 sheets only are selected down below, and that "Select" is highlighted to the right (not hover or menu), then click OK twice

- right click to duplicate the original dashboard once again (not the filtered dashboard)
- dashboard > actions > add action > highlight
- name it "Region Highlight"
- make sure source is the same as before (only the 1st sheet as source, and flipped down below (target sheets are the 2nd and 3rd))
- make sure "Menu" is selected in blue
- hit OK and OK
- select the pie chart
- worksheet > tooltip
- change dropdown to be "on hover", OK
- hover over pie chart section, then click on the link in the tooltip popup to highlight all charts

- make a brand new dashboard with the new dashboard icon down below
- change size to automatic
- drag in sales distr. by state
- X to close legends on the right
- make sure Tiled is selected in the "Objects" card to the bottom right, and then drag the "web page" pill to the right hand side of the map
- Add the URL (https://en.wikipedia.org/wiki/Wikipedia) and then hit OK
- dashboard > actions > add action > go to URL
- name it "State URL"
- change from "Hover" to "Select"
- paste into URL section "https://en.wikipedia.org/wiki/ " and then click on the right caret & select "State"
( the URL input should show this: https://en.wikipedia.org/wiki/<State> )
- hit OK and OK

easy online saving:
- at the top of the screen, click server > tableau public > save to tableau public

* you can export to PDF
* you can export as a packaged workbook so others can interact with this document as well

"tableau server you are publishing to does not permit external database connections"







notes:

- measures: numeric things that span over ranges such as binaries, quantities, geo-coordinates, percentages, frequencies. "continuous"

- dimensions: typically non-range, string data such as ID's, names, categories. Also includes places (but not lat, long) & dates. categories can encompass/represent measures. "discrete" 

https://public.tableau.com/profile/avi.drucker#!/vizhome/SalesDistributionDashboards/Dashboard4?publish=yes