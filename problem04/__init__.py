import check50
import check50.c

@check50.check()
def exists():
    """problem04.c exists"""
    check50.exists("problem04.c")

@check50.check(exists)
def compiles():
    """problem04.c compiles"""
    check50.c.compile("problem04.c", lcs50=True)

@check50.check(compiles)
def problem04():
    """problem04.c prints \"expected pattern\""""
    check50.run("./problem04").stdout("42\n\n8\n\n88\n88\n\n888\n888\n888\n\n8888\n8888\n8888\n8888\n\n42\n").exit()