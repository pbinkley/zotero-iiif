# zotero-iiif
Exploration of how to add IIIF capabilities to Zotero


This exploration was prompted by discussion of various integration by the IIIF community at the [2022 Online Meeting](https://iiif.io/event/2022/online-meeting/). I thought there might be a doable project to create a Zotero plugin that would capture IIIF manifest URIs, store them in captured Zotero records, and make it easy to call them up them in a IIIF viewer. I posted about this on the [Zotero Forum](https://forums.zotero.org/discussion/101597/iiif-plugin-proposal?new=1). I'll use this repo for anything shareable that comes out of this exploration.

## 0. Basic approach

Low-tech way of storing and using a #IIIF manifest uri in #Zotero: 

\1. In a Zotero item: "Add Attachment" -> "Add Link to URI", paste the manifest URI, give it the title "IIIF Manifest". 

\2. Add this bookmarklet to your browser: 

```
javascript:o=location.href;location.href='https:\/\/uv-v4.netlify.app\/#?manifest='+o
```

Call it "UV". 

\3. Double-click the IIIF Manifest link in the Zotero item; when it opens the manifest in your browser, click the UV bookmarklet to open it in Universal Viewer.

That sets the bar pretty low for some kind of improved service.
