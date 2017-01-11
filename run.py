
import csv
import time
import logging
import configparser

from emailer.emailer import send_email
import emailer.logging_utils as logutils

__author__ = 'damirah'
__email__ = 'damirah@live.com'


def load_config():
    """
    Load and return app configuration
    :return:
    """
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    return cfg


if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    cfg = load_config()

    delay = cfg['sending']['delay']
    text_path = cfg['text']['text']
    subject = cfg['text']['subject']
    emails_file = cfg['headers']['to']
    from_address = cfg['headers']['from']
    copy_address = cfg['headers']['copy']
    emails_list = []

    logger.info('From: {}, copy: {}, delay: {}'
                .format(from_address, copy_address, delay))
    logger.info('Subject: {}'.format(subject))

    with open(text_path, 'r') as fp:
        text = fp.read()

    logger.info('Text: {}'.format(text))

    with open(emails_file, 'r') as fp:
        reader = csv.reader(fp)
        for row in reader:
            if len(row) > 3:
                logger.warn('Error, will not send to: {}'.format(row))
            else:
                emails_list.append({
                    'first_name': str(row[0]).strip(),
                    'last_name': str(row[1]).strip(),
                    'address': str(row[2]).strip()
                })

    logger.info('Will send {} emails'.format(len(emails_list)))

    processed = 0
    total = len(emails_list)
    how_often = logutils.how_often(total)

    for email in emails_list:
        send_email(from_address, copy_address,
                   email['address'], email['first_name'], subject, text)
        logger.info('Sent email to: {} {} ({})'.format(
            email['first_name'], email['last_name'], email['address']))
        processed += 1
        if processed % how_often == 0:
            logger.debug(logutils.get_progress(processed, total))
        time.sleep(delay)
