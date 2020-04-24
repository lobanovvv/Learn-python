# Packges is directory in this location with __init__ file and a lot of modules include.

# Set 1
import packagesDir.moduleInPackage
packagesDir.moduleInPackage.messagesPrint()

# Set 2
from packagesDir import moduleInPackage # , otherModules
moduleInPackage.messagesPrint()

# Set 3
from packagesDir.moduleInPackage import messagesPrint
messagesPrint()
