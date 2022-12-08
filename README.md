# zotero-iiif
Exploration of how to add IIIF capabilities to Zotero


This exploration was prompted by discussion of various integration by the IIIF community at the [2022 Online Meeting](https://iiif.io/event/2022/online-meeting/). I thought there might be a doable project to create a Zotero plugin that would capture IIIF manifest URIs, store them in captured Zotero records, and make it easy to call them up them in a IIIF viewer. I posted about this on the [Zotero Forum](https://forums.zotero.org/discussion/101597/iiif-plugin-proposal?new=1). I'll use this repo for anything shareable that comes out of this exploration.

## 0. Basic approach

Low-tech way of storing and using a #IIIF manifest uri in #Zotero: 

Step 1. In a Zotero item: "Add Attachment" -> "Add Link to URI", paste the manifest URI, give it the title "IIIF Manifest". 

Step 2. Add this bookmarklet to your browser: 

```
javascript:o=location.href;location.href='https:\/\/uv-v4.netlify.app\/#?manifest='+o
```

Call it "UV". 

Step 3. Double-click the IIIF Manifest link in the Zotero item; when it opens the manifest in your browser, click the UV bookmarklet to open it in Universal Viewer.

That sets the bar pretty low for some kind of improved service.

## 1. A Lookup Engine Using a Field

In this approach we specify a lookup engine that will appear in the dropdown by the green arrow above the item view. I don't know how to make a lookup engine retrieve an attached link (and I think it may not be possible), so for this demo I'll put the manifest URI in the "Loc. in Archive" field. It's used in the ```_urlTemplate``` value. If you'd rather use a different field, codes can be found [https://aurimasv.github.io/z2csl/typeMap.xml](here) (use the name in the "Zotero type" column).

Follow the instructions on [adding lookup engines](https://www.zotero.org/support/locate).

```
	{
		"_name": "IIIF",
		"_alias": "IIIF",
		"_description": "Render IIIF Manifest in UV",
		"_icon": "https://iiif.io/assets/favicon.ico",
		"_hidden": false,
		"_urlTemplate": "https://uv-v4.netlify.app/#?manifest={z:archiveLocation}",
		"_urlParams": [],
		"_urlNamespaces": {
			"z": "http://www.zotero.org/namespaces/openSearch#",
			"": "http://a9.com/-/spec/opensearch/1.1/"
		},
		"_iconSourceURI": "https://iiif.io/assets/favicon.ico"
	}
```

This works, but only at the expense of hijacking an existing field. Next step: dig into whether there's a namespace that would let a lookup engine access the "IIIF Manifest" attached link.
