#!/usr/bin/env python

import os, os.path, shutil, datetime, glob, stat, time

""" 
Usage:
    source = '/path/to/source'
    dest = '/path/to/dest'
    
    from rotatingbackup import TimedRotatingBackup
    trb = TimedRotatingBackup(source, dest, 'd', 1, 5)
    trb.backup()
"""

__author__ = """leopku<leo.ss.pku@gmail.com>"""
__version__ = 0.1
__docformat__ = 'plaintext'

#_MIDNIGHT = 24 * 60 * 60  # number of seconds in a day

class BaseRotatingBackup:
    """
    Base class for rotating backup files at a certain point.
    Not meant to be instantiated directly. Instead, use RotatingFile.
    """
    def __init__(self, source, destpath):
        """
        Use the specified pathname/filename for backup
        source is the file or path which you want to backup
        destpath is the path whick you want to backup to.
        make sure destpath is exists, otherwise you should create it first.        
        """
        self.destpath = destpath
        self.source = source
        self.baseName = os.path.basename(self.source)
        
    def backup(self):
        """
        backup self.source to self.destpath
        """
        if self.shouldRollover():
            self.doRollover()
        
class CountedRotatingBackup(BaseRotatingBackup):
    """
    Rotating backup files, which switches from one file to the next
    """
    def __init__(self, source, destpath, backupCount=0):
        """
        If backupCount  is >= 1, the system will successively move older files
        with the same filename/pathname as the base file, but with extensions
        ".1", ".2" etc. append to it.
        """
        BaseRotatingBackup.__init__(self, source, destpath)
        self.backupCount = backupCount
        
    def doRollover(self):
        """
        Do a rollover
        """
        dest = os.path.join(self.destpath, self.baseName)
        for i in range(self.backupCount-1, 0, -1):
            sfn = "%s.%d" % (dest, i)
            dfn = "%s.%d" % (dest, i + 1)
            if os.path.exists(sfn):
                if os.path.exists(dfn):
                    delete(dfn)
                os.renames(sfn, dfn)
        if os.path.exists(dest):
            os.rename(dest, dest + '.1')
        copy(self.source, dest)
            
    def shouldRollover(self):
        if self.backupCount > 0:
            return 1

class SizedRotatingBackup(BaseRotatingBackup):
    """
    Backup files while file exceed sized.
    if file size > maxBytes, while rollover is done, no more than backupCount files are kept - the oldest ones are deleted.
    """
    def __init__(self, filename, destpath, maxBytes=0, backupCount=0):
        """
        this class now only process files, directoris no acceptable
        """
        if not os.path.isfile(filename):
            raise 'first parameter should be a file'
        BaseRotatingBackup.__init__(self, filename, destpath)
        self.filename = filename
        self.maxBytes = maxBytes
        self.backupCount = backupCount
        
    def doRollover(self):
        dest = os.path.join(self.destpath, self.baseName)
        for i in range(self.backupCount-1, 0, -1):
            sfn = "%s.%d" % (dest, i)
            dfn = "%s.%d" % (dest, i + 1)
            if os.path.exists(sfn):
                if os.path.exists(dfn):
                    delete(dfn)
                os.renames(sfn, dfn)
        if os.path.exists(dest):
            os.rename(dest, dest + '.1')
        copy(self.source, dest)
    
    def shouldRollover(self):
        fileStats = os.stat(self.filename)
        if fileStats[stat.ST_SIZE] >= self.maxBytes:
            return 1
        return 0
        
class TimedRotatingBackup(BaseRotatingBackup):
    """
    Backup files/direcotries at certain timed intervals.
    If backupCount is > 0, when rollover is done, no more than backupCount files are kept - the oldest ones are deleted.
    """
    def __init__(self, source, destpath, when='h', interval=1, backupCount=0):
        BaseRotatingBackup.__init__(self, source, destpath)
        self.when = when.upper()
        self.backupCount = backupCount
        # Calculate the real rollover interval, which is just the number of
        # seconds between rollovers.  Also set the filename suffix used when
        # a rollover occurs.  Current 'when' events supported:
        # S - Seconds
        # M - Minutes
        # H - Hours
        # D - Days
        # W{0-6} - roll over on a certain day; 0 - Monday
        #
        # Case of the 'when' specifier is not important; lower or upper case
        # will work.

        if self.when == 'S':
            self.interval = 1 # one second
            self.suffix = "%Y-%m-%d_%H-%M-%S"
        elif self.when == 'M':
            self.interval = 60 # one minute
            self.suffix = "%Y-%m-%d_%H-%M"
        elif self.when == 'H':
            self.interval = 60 * 60 # one hour
            self.suffix = "%Y-%m-%d_%H"
        elif self.when == 'D':
            self.interval = 60 * 60 * 24 # one day
            self.suffix = "%Y-%m-%d"
        elif self.when.startswith('W'):
            self.interval = 60 * 60 * 24 * 7 # one week
            if len(self.when) !=2:
                raise ValueError('You must specify a day for weekly rollover from 0 to 6 (0 is Monday): %s' % self.when)
            if self.when[1] < '0' or self.when[1] > '6':
                raise ValueError('Invalid day specified for weekly rollover: %s' % self.when)
            self.dayOfWeek = int(self.when[1])
            self.suffix = "%Y-%m-%d"
        else:
            raise ValueError('Invalid rollover interval specified: %s' % self.when)
        
        self.interval = self.interval * interval #multiply by units requested
        #self.lastBackupPoint,  self.abandonedBackupPoint = self.getBackupPoints()
            
    def getBackupPoints(self, action='get'):
        lastBackupPoint = '1900-00-00'
        dest = os.path.join(self.destpath, self.baseName)
        allbackups = glob.glob(dest + '.20*')
        allbackups.sort()
        count = len(allbackups)
        if count > 0:
            if action == 'delete' and count >= self.backupCount:
                num = count - self.backupCount + 1
                for i in range(num):
                    delete(allbackups[i])
            lastBackupPoint = allbackups[-1].split('.')[-1]
        return lastBackupPoint
    
    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        self.getBackupPoints('delete')
        currentTime = datetime.datetime.today()
        dfh = os.path.join(self.destpath, self.baseName + '.' + time.strftime(self.suffix, currentTime.timetuple()))
        copy(self.source, dfh)

    def shouldRollover(self):
        """
        should we do a rollover
        """
        currentTime = datetime.datetime.today()
        if self.backupCount <= 0:
            return 0
        result = 1
        lastBackupPoint = self.getBackupPoints()
        if lastBackupPoint > '1900-00-00':
            # next line can only run at python 2.5 or above.
            # lastRolloverTime = datetime.datetime.strptime(lastBackupPoint, self.suffix)
            # if you are using python 2.4 or blow
            # using next three lines instead.
            t = time.strptime(lastBackupPoint, self.suffix)
            lastRolloverTime = datetime.datetime(*t[:6])
            # above three lines python 2.4 compatible
            nextRolloverTime = lastRolloverTime + datetime.timedelta(seconds = self.interval)
            if currentTime < nextRolloverTime:
                result = 0
        return result
            
def copy(source, destination):
    """
    Copy a file or path
    """
    if os.path.isfile(source):
        shutil.copyfile(source, destination)
    else:
        shutil.copytree(source, destination)
        
def delete(path):
    """
    Delete a file or path
    """
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)