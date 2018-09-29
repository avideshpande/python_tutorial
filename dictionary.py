thisdict = {
	"brand" : "Ford",
	"model": "Mustang",
	"year" : 1984
	}
print(thisdict)
print(thisdict["model"])
print(thisdict.get("model"))

del thisdict["model"]
print(thisdict)	