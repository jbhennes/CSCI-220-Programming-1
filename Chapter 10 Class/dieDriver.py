from die2 import Die

def main():
    kens = Die()
    jesses = Die()

    print "Objects at:"
    print "kens", kens
    print "jesses", jesses
    print

    print "The values:"
    print "kens:", kens.getFaceValue()
    jV = jesses.getFaceValue()
    print "jesses:", jV
    print

    kens.setFaceValue(5)
    jesses.setFaceValue(3000)
    print "The values:"
    print "kens:", kens.getFaceValue()
    jV = jesses.getFaceValue()
    print "jesses:", jV
    print

    jesses.setFaceValue(0)
    print "The values:"
    jV = jesses.getFaceValue()
    print "jesses:", jV

    jesses.setFaceValue(-5)
    print "The values:"
    jV = jesses.getFaceValue()
    print "jesses:", jV

    jesses.setFaceValue(6)
    print "The values:"
    jV = jesses.getFaceValue()
    print "jesses:", jV

    print "The values:"
    kens.roll()
    jesses.roll()
    print "kens:", kens.getFaceValue()
    jV = jesses.getFaceValue()
    print "jesses:", jV
    print

    print "Objects at:"
    print "kens", kens
    print "jesses", jesses
    print
    print "Done"

main()
