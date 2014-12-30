#assigns variable formatter to four raw data formatting specifiers
formatter = "%r %r %r %r"

#prints formatter subbed for integers
print formatter % (1, 2, 3, 4)
#prints formatter specifier subbed for strings
print formatter % ("one", "two", "three", "four")
#prints formatter subbed for information stored in a variable
print formatter % (formatter, formatter, formatter, formatter)
#prints formatter subbed for strings
print formatter % (
  "I had this thing.",
  "That you could type up right.",
  "But it didn't sing.",
  "So I said goodnight."
)
