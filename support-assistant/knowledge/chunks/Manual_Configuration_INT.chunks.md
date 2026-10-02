<!-- chunk 1 | 219 tokens | part 1/1 -->
Manual section: Introduction > How do I configure MedicalPortal?

Goal

Our goal is to provide you with a clear and practical overview of all the steps needed to: Setup MedicalPortal optimally.

MedicalPortal is made up of various elements that you can configure step by step. This configuration manual has been prepared to help you with this and provides a clear explanation of how to use each element of MedicalPortal furnishings Sometimes there are interdependencies between the elements. This is taken into account in this document.

The manual has the same order as the maintenance menu in MedicalPortal. The basic configuration is discussed, such as configuring Core, but also the more complex parts. We discuss, among other things, setting up forms, setting up appointments and configuring the financial module. We also pay attention to the patient-related configuration.

---

<!-- chunk 2 | 93 tokens | part 1/1 -->
Manual section: Introduction > Who or what else can I consult?

In addition to an explanation in this manual, we refer, where relevant, to videos on YouTube. These videos mainly focus on how to use MedicalPortal, but sometimes also provide valuable context for configuration.

If you still have questions despite this manual, you can always contact the Heart for Health team.

---

<!-- chunk 3 | 76 tokens | part 1/1 -->
Manual section: Messages

It is possible to sign in to all users MedicalPortal show a message. This message appears as a pop-up window for all logged in users and can also be read below Info → Messages. In MedicalPortal it is possible to share two types of messages: General messages and Release messages.

---

<!-- chunk 4 | 186 tokens | part 1/1 -->
Manual section: Messages > General messages

Creating and publishing a new general message is done as follows:

1. Go to Maintenance → Messages - General messages
2. Click at the top right + General message
3. Fill in the fields in the window
   1. Title: This will be the title of the pop-up window
   2. Short message: This message will be shown in the pop-up window
   3. Full message: an expanded version of the message that is shown when the user clicks Read more
4. Click on Save
5. Click on Publish (which appears when the cursor hovers over the message)
6. Click on Confirm

When you click Confirm the message will be published and immediately visible to the users. Once a post has been published it cannot be withdrawn, edited or deleted.

---

<!-- chunk 5 | 256 tokens | part 1/1 -->
Manual section: Messages > Release concepts

Release messages are similar to general messages, but are specific to releases. It can show a note to the users before a release or a message regarding the released new version of MedicalPortal. Preparing and publishing a release message is as follows:

1. Go to Maintenance → Messages - Release messages
2. Click at the top right + Concept
3. Fill in the fields in the window
   1. Title: This will be the title of the pop-up window
   2. Short message: This message will be shown in the pop-up window
   3. Full message: an expanded version of the message that is shown when the user clicks Read more
   4. Type: concerns the message type: New version or Before release
4. Click on Save
5. Click on Activate (which appears when the cursor hovers over the message)
6. Click on Confirm

When the message has only been saved, it still has the status of inactive. Once the release message is published, as described above, the message can no longer be withdrawn, modified or deleted.

---

<!-- chunk 6 | 202 tokens | part 1/1 -->
Manual section: Finance > Administrations > Why add an administration?

The equipment required for the financial settlement of care is located below Maintenance → Finance and covers several parts.

Here you determine to which administration(s) the care provided will be recorded. This is an important aspect for a clear and error-free financial settlement. In the administration you can manage the Maintenance of the financial details and the invoice Maintenance.

It is possible to manage multiple administrations. This is desirable in situations where, for example:

* A distinction is made between bank accounts on which the care is booked.
* A new or different AGB code is used.
* A different invoice numbering is used for different administrations.
* A different logo is used for different administrations.

---

<!-- chunk 7 | 218 tokens | part 1/1 -->
Manual section: Finance > Administrations > How to add an administration?

Follow the steps below to add a new administration:

1. Go to Maintenance → Finance - Administrations
2. Click at the top right + Administration
3. Fill in the required information for administration. The available fields are explained in the Administration Fields table.
4. Click on Save

The new administration is now being added and is immediately available

**TIPS** to add an administration:

* Vecozo email address is important for communication with the Vecozo services.
* DIS data is important for deliveries to DIS.
* Without an AGB code, you cannot submit a claim to a health insurer
* Per bank account number where turnover is received for declarations from MedicalPortal there must be an administration.
* The logo for the letters must be uploaded here (on the production environment).

---

<!-- chunk 8 | 104 tokens | part 1/1 -->
Manual section: Finance > Administrations > Do you want to change or delete an administration?

Follow the steps below to change or delete an existing administration:

1. Go to Maintenance → Finance - Administrations
2. Go to the relevant administration line with your cursor.
3. Click on the pencil icon, if you want to change the administration.
4. Click on the trash icon, if you want to delete the administration.

---

<!-- chunk 9 | 510 tokens | part 1/2 -->
Manual section: Finance > Administrations > Table: Administration fields

| **Field** | **Explanation** |
| --- | --- |
| **General** | |
| Administration code | Unique identification code for an administration. This can be seen in the ledger |
| Name | Name of the administration. This is popular in several places MedicalPortal to see again. For example on an invoice. |
| Land | Country of administration |
| Address/PO Box | Address or PO box of the administration |
| Mailbox | Administration PO box |
| Address (street, number, addition, zip code, city) | Address of the administration |
| AGB-code | AGB code of the healthcare institution. This number is used when declaring |
| URA code | Unique number of a healthcare institution for electronic communication of healthcare data |
| Phone number | Administration telephone number |
| E-mail | E-mail address of the administration. This is visible on the PDF invoices |
| File name (logo) | Logo of the administration. This is visible on certain invoices |
| **Financial details** | |
| Account holder | Name of the administration account holder |
| Bank account number | The bank account number that belongs to the administration |
| IBAN | The IBAN number that belongs to the administration. This is visible on the PDF invoices |
| Correspondent bank name | Name of the bank of the Bank account number |
| Correspondentbank SWIFT | SWIFT code for the bank of the Bank account number |
| Company Registration IF | Company Registration ID of the healthcare institution whose administration is held |
| Organization Category ID | Organization number of the healthcare institution whose administration is held |
| TAX-ID | VAT number of the healthcare institution whose administration is held |
| Standard currency | The default currency for administration. |
| DIS: Setting Number | The unique number for the institution to be able to carry out the DIS delivery |
| DIS: Username DIS | The username of the institution to be able to carry out the DIS delivery |
| Billing Maintenance | |

---

<!-- chunk 10 | 515 tokens | part 2/2 -->
Manual section: Finance > Administrations > Table: Administration fields

| **Field** | **Explanation** |
| --- | --- |
| Financial period | Only the Invoice date option is possible here. |
| Invoice number length | The length of the invoice number for administration. For example: 5. When the number of invoices exceeds the configured invoice number length, the length is automatically adjusted. However, the configured length remains visible in the administration settings |
| Invoice prefix | The prefix that is placed before the invoice number. These can be both numbers and letters. For example: 222 or healthcare institution |
| Last invoice number | This is the last invoice number used for this administration. This number is automatically updated, but can also be changed. A change in the last invoice number directly affects the number of the next invoice that is created. |
| Proforma prefix | The prefix that is placed before the quotation number. These can be both numbers and letters. For example: 222 or healthcare institution |
| Latest proforma invoice number | This is the last quotation number used for this administration. This number is automatically updated, but can also be changed. A change in the last invoice number directly affects the number of the next invoice that is created. |
| Invoice period (in days) | The Invoice period is the payment period in which the patient can pay the invoice. This period is used for the PDF invoices.  For example:   * Completed: 14 (days) * When the invoice is created, the payment term is calculated for the patient or organization: today + 14 days” |
| Reminder period (in days) | The reminder period is the period set between sending the original invoice and sending a payment reminder.  For example:   * Completed 14 (days) |
| Final notice period (in days) | The final notice period is the period between sending a payment reminder and sending a reminder.  For example:   * Completed 14 (days) |
| VeCoZo email | Vecozo email address is important for communication with the Vecozo services. |

---

<!-- chunk 11 | 144 tokens | part 1/1 -->
Manual section: Finance > Automation > Bulk Closing DBC’s

You can use automation to take manual actions off your hands and have them carried out periodically by the system.

Set the status of this process to On to have the system automatically close all DBCs that are eligible for closure every night. The drop-down list allows you to set the end date until which the system attempts to close DBCs. You can use this, for example, to close DBCs that have not yet ended very recently. This way you can give users the opportunity to make some adjustments before the DBC is closed.

---

<!-- chunk 12 | 46 tokens | part 1/1 -->
Manual section: Finance > Automation > Bulk grouping DBCs

Set the status of this process to On to have the system automatically group all DBCs that are eligible for grouping every night.

---

<!-- chunk 13 | 76 tokens | part 1/1 -->
Manual section: Finance > Automation > Import

Set the status of this process to On to allow the system to automatically import all DBCs and activities that are eligible for import every night. The drop-down list allows you to set the end date until which the system attempts to import DBCs and activities.

---

<!-- chunk 14 | 176 tokens | part 1/1 -->
Manual section: Finance > Cost Bearers/Cost Centers > Why add Cost Bearers or Cost Centers?

Cost Bearers and locations are set up to ensure that the invoiced care is posted to the correct general ledger account. Cost Centers are used for Departments or divisions, for example, and cost objects are units, such as projects. Both costs and revenues are posted to Cost Bearers and locations. Depending on how the organization is structured, multiple Cost Centers and/or Cost Bearers can be set up. 1 Cost Centers and 1 Cost Bearers are required per organization. This means that all care resulting from appointments in a specific Departments and/or agenda can be booked to preset Cost Bearers and locations.

---

<!-- chunk 15 | 104 tokens | part 1/1 -->
Manual section: Finance > Cost Bearers/Cost Centers > Add Cost Bearers or Cost Centers

Follow the steps below to add a new Cost Bearers:

1. Go to Maintenance → Finance - Cost Bearers/Cost Centers.
2. Click at the top right + Cost Bearers/ + Cost Centers.
3. Enter the required data for the Cost Bearers/Cost Centers.
4. Click on Save.

The new Cost Bearers/Cost Centers are now added and are immediately available.

---

<!-- chunk 16 | 145 tokens | part 1/1 -->
Manual section: Finance > Cost Bearers/Cost Centers > Changing or archiving/activating a Cost Bearers or Cost Centers

Follow the steps below to change or archive an existing cost object:

1. Go to Maintenance → Finance - Cost Bearers/Cost Centers.
2. Move the cursor over the line of the relevant Cost Bearers/Cost Centers.
3. Click on the pencil icon to change the Cost Bearers/Cost Centers.
4. Click on the archive icon to archive the Cost Bearers/Cost Centers, this Cost Bearers is then no longer active.
5. Click on the activate icon to activate the Cost Bearers/Cost Centers.

---

<!-- chunk 17 | 229 tokens | part 1/1 -->
Manual section: Finance > Cost Bearers/Cost Centers > Where are Cost Bearers and locations used in MedicalPortal?

In various places MedicalPortal the Cost Bearers and locations can be selected, these are:

* When adding/changing a Departments Maintenance → Core - Departments.
* When manually adding/changing a patient activity.
* When adding/changing a registration code Maintenance → Finance - Registration codes.
* When adding/changing a declaration code Maintenance → Finance - Declaration codes.
* When adding/changing a resource, room or bed at Maintenance → Agenda - Resources.
* When adding/changing a package at Maintenance → Order forms - Measurements.

The Cost Bearers and location on which an activity is ultimately recorded is chosen using the waterfall method where it is checked in this specific order:

1. Departments
2. Activity/registration code/package
3. Declaration code
4. Resource, Room or bed

---

<!-- chunk 18 | 101 tokens | part 1/1 -->
Manual section: Finance > Currency Exchange

If declaration codes are subject to VAT, a VAT percentage can be set per declaration code. Subsequently, each declaration code is entered in the price matrix indicates which of these VAT percentages should be used for the relevant declaration code (and financial flow). The VAT percentage and amount are shown on the invoices submitted MedicalPortal are made.

---

<!-- chunk 19 | 145 tokens | part 1/1 -->
Manual section: Finance > Currency Exchange > Add VAT percentage

Follow the steps below to add a new VAT percentage:

1. Go to Maintenance → Finance - VAT.
2. Click at the top right + Currency Exchange.
3. Enter the name for the relevant VAT percentage.
4. Enter the VAT percentage.

**NB:** ANDr a certain percentage is only allowed once per type (including/exclusive). Therefore, double percentages cannot occur per type.

5. Select for type whether the percentage for prices includes or excludes VAT. Click Save.

The new VAT percentage is now added and is immediately available.

---

<!-- chunk 20 | 122 tokens | part 1/1 -->
Manual section: Finance > Currency Exchange > Change or archive/activate a VAT percentage

Follow the steps below to change or archive an existing VAT percentage:

1. Go to Maintenance → Finance - Currency Exchange.
2. Move the cursor over the line of the relevant VAT percentage.
3. Click on the pencil icon to change the VAT percentage.
4. Click on the archive icon to archive the VAT percentage, it is then no longer active.
5. Click on the activate icon to activate the VAT percentage.

---

<!-- chunk 21 | 249 tokens | part 1/1 -->
Manual section: Finance > Declaration codes

Declaration codes are established by the NZa (insured healthcare), or self-designed codes for which a price can be quoted. In the case of insured care, the declaration code is derived from the registration codes sent to the grouper.
In the case of self-configured codes, the relationship between registration codes and declaration codes is established themselves (see 'Registration codes').

All NZa declaration codes will be added automatically using the Import DBC system. The declaration codes for the DBCs are located in the declaration code category DBCNLBASE and for activities to be invoiced separately in the declaration code category NLBASE. If there are new releases from the NZa, they can be found via Maintenance → Finance - Import DBC system. For declaration codes other than those of the NZa, it is possible to create a different declaration code category, for example for uninsured care for which your own declarations have been created.

---

<!-- chunk 22 | 131 tokens | part 1/1 -->
Manual section: Finance > Declaration codes > Add category declaration code

Follow the steps below to add a new registration code category:

1. Go to Maintenance → Finance - Declaration codes.
2. Click at the top left + Declaration code categories.
3. Enter a short description of the declaration code category.
4. Enter a long description of the declaration code category.
5. Optionally enter the Cost Bearers and Cost Centers.
6. Click on Save.

The new declaration code category has been added and immediately available.

---

<!-- chunk 23 | 106 tokens | part 1/1 -->
Manual section: Finance > Declaration codes > Change/delete category declaration code

Follow the steps below to change or archive a registration code category:

1. Go to Maintenance → Finance - Declaration codes.
2. Move the cursor over the line of the relevant declaration code category.
3. Click on the pencil icon to change the declaration code category.
4. Click on the trash icon to remove the category declaration code.

---

<!-- chunk 24 | 153 tokens | part 1/1 -->
Manual section: Finance > Declaration codes > Add declaration code

Follow the steps below to add a new registration code category:

1. Go to Maintenance → Finance - Declaration codes.
2. Click at the top left + Code.
3. Enter the category declaration code.
4. Enter the declaration code.
5. Enter the short description of the declaration code.
6. Enter the long description of the declaration code.
7. Optionally enter the Cost Bearers and Cost Centers.
8. Click on Save.

The new declaration code has been added and is immediately available. A price can then be linked to a declaration code in the Price Matrix.

---

<!-- chunk 25 | 209 tokens | part 1/1 -->
Manual section: Finance > Registration codes

Registration codes are established by the NZa (insured care) or self-designed codes that are linked to an investigation for, for example, uninsured care. By setting up an examination within an appointment, the registration codes are added to the patient's activity registration.

All NZa registration codes for insured care are automatically added through the DBC import. These registration codes are in the registration code category NLBASE. If there are new releases from the NZa, they can be found via the Import DBC system (Maintenance → Finance - Import DBC system) are imported. In addition, custom registration codes can also be added. For registration codes other than those of the NZa, it is possible to create a different registration code category, for example for uninsured care.

---

<!-- chunk 26 | 130 tokens | part 1/1 -->
Manual section: Finance > Registration codes > Add category registration code

Follow the steps below to add a new registration code category:

1. Go to Maintenance → Finance - Registration codes.
2. Click at the top left + Registration code categories.
3. Enter the name of the registration code category.
4. Enter the description of the registration code category.
5. Optionally enter the Cost Bearers and Cost Centers.
6. Click on Save.

The new registration code category has been added and is immediately available.

---

<!-- chunk 27 | 117 tokens | part 1/1 -->
Manual section: Finance > Registration codes > Change/archive category registration code

Follow the steps below to change or archive a registration code category:

1. Go to Maintenance → Finance - Registration codes.
2. Move the cursor over the line of the relevant registration code category.
3. Click on the pencil icon to change the registration code category.
4. Click on the archive icon to archive the registration code category, it will then no longer be active.

---

<!-- chunk 28 | 238 tokens | part 1/1 -->
Manual section: Finance > Registration codes > How to add a registration code?

Follow the steps below to add a new registration code:

1. Go to Maintenance → Finance - Registration codes.
2. Click at the top right + Registration code.
3. Enter the category registration code.
4. Enter the registration code.
5. Enter the description of the registration code.
6. The start date is automatically set to today's date, which can be changed.
7. Optionally enter an end date.
8. Optionally enter a Cost Bearers and Cost Centers.
9. If a price must be linked to the registration code, add a declaration code by clicking on + Add declaration code and then follow these steps:
   1. Enter the category declaration code.
   2. Enter the declaration code.
   3. The start date is automatically set to today's date, which can be changed.
   4. Optionally enter an end date.
10. Click on Save.

The new registration code has been added and is immediately available.

---

<!-- chunk 29 | 111 tokens | part 1/1 -->
Manual section: Finance > Registration codes > How to change/archive a registration code?

Follow the steps below to change or archive a registration code category:

1. Go to Maintenance → Finance - Registration codes.
2. Move the cursor over the line of the relevant registration code.
3. Click on the pencil icon to change the registration code.
4. Click on the archive icon to archive the registration code, it will then no longer be active.

---

<!-- chunk 30 | 81 tokens | part 1/1 -->
Manual section: Finance > Price matrix

The price matrix is the place to register prices from organizations (health insurers, your own rate or the passer-by rate) per declaration code. Correct design of the price matrix ensures that the care is invoiced with the correct rate, invoice type and any discount or VAT percentage.

---

<!-- chunk 31 | 487 tokens | part 1/2 -->
Manual section: Finance > Price matrix > How to set up a correct price matrix? > Price matrix fields for matching

In the invoicing process, a rate is selected based on a match in the price matrix when importing a care registration (DBC or activity). Fields that are used from the healthcare registration to make this match are: Declaration code (required), Date (required), Financial flow (required), Debtor Type (required), Debtor (via the COV check), Package code (via the COV check). ), Departments, Location and Specialty.
Fields in the price matrix that are used to match the healthcare registration: Declaration code, Start date, End date, Financial flow, Organization, Organization group, Insurance package code, Departments, Location, Specialty.
**TIP:** It is important to fill in the above fields in the price matrix lines correctly. The matching process follows a waterfall method, where fields are checked in the order described above to find the most accurate match.

The fields can be completed as follows:

* Declaration code (required): here you can choose a declaration code that has been entered at Maintenance → Finance - Declaration codes.

* Start date (required) and End date: by filling these fields you can check the validity of the price matrix record. The price matrix record is valid for healthcare registrations in which the start date falls within the period of the Start and End Date of the price matrix record.

* Financial flow (required): This field allows you to indicate which financial flow the price matrix follows.

* Organization: You can choose to use the price matrix record to be categorized by organization (health insurer). For example, you choose an organization with the Insurance Company type or another organization to which you want to invoice. The organization must first be entered at Maintenance → Core - Organizations. This field cannot be filled in when the Organization group field is filled.

---

<!-- chunk 32 | 477 tokens | part 2/2 -->
Manual section: Finance > Price matrix > How to set up a correct price matrix? > Price matrix fields for matching

* Organization group: You can choose to use the price matrix record categorized by organization groups. To do this, you choose an organization group that has been entered at Maintenance → Finance - Organization groups. This field cannot be filled in when the Organization field is filled. When this field is filled, the price matrix record is only valid for care registrations whose start date falls within the period of the Start and End Date of the organization group (see chapter Organization groups).

* start date of the care registration must be in the period of the organizational group (wan)

* Insurance package code: You can choose to use the price matrix record to categorize by an insurance package code. You do this, for example, if you do not have a contract for a specific insurance package code. To do this, you choose a package code that is entered at Maintenance → Core - Organization with type Insurance Company -> Contracts. This field can only be filled in when the Organization field is filled.

* Departments: You can choose to use the price matrix record categorized by Departments. To do this, you choose a Departments that has been entered at Maintenance → Core - Departments.

* Location: You can choose to use the price matrix record categorized by locations. To do this, you choose a location that has been entered at Maintenance → Core - Locations.

* Specialty: You can choose to: price matrix record categorized by specialization. You choose a Specialty that has been entered at Maintenance → Core - Specialties.

**TIP:** Make the price matrix as generic as possible. As soon as you introduce differentiations such as organization, location or Departments, the rate will only increase MedicalPortal be chosen if the care registration meets all these conditions.

---

<!-- chunk 33 | 53 tokens | part 1/2 -->
Manual section: Finance > Price matrix > How to set up a correct price matrix? > Pricing matrix fields for billing

In the billing fields below you can indicate how and at what prices the care should be invoiced.

---

<!-- chunk 34 | 513 tokens | part 2/2 -->
Manual section: Finance > Price matrix > How to set up a correct price matrix? > Pricing matrix fields for billing

* Force administration: The administration on which the rate is booked is determined based on the Departments and location of the care registration. If you wish to book turnover from a rate, for example uninsured care, to a different account number, you can also force an administration in the price matrix. The rate will then be forcibly posted to the account number of the chosen administration (provided the ledger matrix is also filled in as such).
* Invoice type: There are different invoice types available in MedicalPortal to declare to the patient or third parties:
  + Vecozo: When declaring from MedicalPortal to health insurer via Vecozo (automatic connection from MedicalPortal) or InfoMedics (no automatic connection). Only allowed with NLDOT financial flow.
  + On paper: When declaring directly to the patient. Both for insured care (non-contracted care and contracted care for foreigners) and non-insured care. Only permitted with financial flow NLDOT and Activity flex.
  + Declaration file: When declaring from MedicalPortal to the health insurer or the patient via InfoMedics. Is only allowed with financial flow Activity.
  + List invoice: When declaring directly to a referring organization or paying agency. This invoice can contain multiple patients. Is only allowed with financial flow Activity.
* Costs: The rate used by your organization or the health insurer for the declaration code.
* Honorarium: If an additional fee applies to declaration codes, you can indicate here which price should be charged.
* VAT: If declaration codes are subject to VAT, you can indicate here which VAT percentages should be used. To do this, first set VAT percentages under Maintenance -> Finance - VAT.
* Discount: A discount may apply to certain declaration codes. You can enter this in this field.
* Exclude cost portion discount and Exclude fee portion discount: Using these options you can disable the Discount and Fee fields.

---

<!-- chunk 35 | 87 tokens | part 1/1 -->
Manual section: Finance > Price matrix > Adding price matrix records

For the (bulk) addition of prices for insured care, please refer to chapter Import DBC system.

To add prices for uninsured care, you must do the following. Is your current price matrix empty? Then we advise you to add manual prices per declaration code (chapter Declaration codes)

---

<!-- chunk 36 | 190 tokens | part 1/1 -->
Manual section: Finance > Price matrix > Adding price matrix records > Single item

1. Go to Maintenance → Finance - price matrix
2. Click at the top right + Price
3. Fill in the required information for the price matrix line
4. Click on Save

The new one price matrix record has been added and can continue immediately MedicalPortal be used.

**TIP:** Make the price matrix as generic as possible. As soon as you introduce differentiations such as organization, location or Departments, the rate will only increase MedicalPortal be chosen if the care registration meets all these conditions.

It is also possible to create price matrix records in bulk. We advise you this if you are going to apply new prices for declaration codes that have already been set up.

---

<!-- chunk 37 | 374 tokens | part 1/1 -->
Manual section: Finance > Price matrix > Adding price matrix records > In Bulk

1. Go to Maintenance → Finance - Price matrix
2. Click at the top right Import prices
3. Click on Download format file
4. Your browser downloads a d file
5. Fill in all relevant fields in this file to import the new prices

**TIP**: The following fields are required to import a rate declaration code, start date, stream, invoice type and mutation.

   - Check carefully whether the fields have been completed correctly. The formats of the fields are described in chapter Format fields in Excel
   - To import new prices, enter the mutation value “1”.

**TIP:** If prices are already known for a declaration code, first ensure that the current prices have an end date.

6. Upload the file by dragging it into the appropriate field
7. Click on Import prices to import the prices
8. The system validates the rules in the import file and then imports the correct prices
9. Once the import is complete, a dialog box appears. This dialog box contains a "Continue to results" button. Clicking "Continue to results" opens a dialog box with an overview of both imported and non-imported prices. For the non-imported records, reasons why the record was not imported are provided. The new price matrix record will be immediately used by MedicalPortal.

**TIP:** To import new prices for a new year, for example, you can first export the existing prices, make the changes in an Excel file and then import the file again entirely.

---

<!-- chunk 38 | 102 tokens | part 1/1 -->
Manual section: Finance > Price matrix > Changing price matrix records > Single item

To change prices (in bulk), you must do the following.

1. Go to Maintenance → Finance - Price matrix
2. Click on it pencil icon of a price matrix line on which you want to make a change
3. Change the desired data
4. Click on Save

Of price matrix record has been changed and can continue immediately MedicalPortal be used.

---

<!-- chunk 39 | 437 tokens | part 1/1 -->
Manual section: Finance > Price matrix > Changing price matrix records > In Bulk

1. Go to Maintenance → Finance - Price matrix
2. Apply filtering to the overview
3. Click at the top right Export prices
   1. Your browser downloads the filtered selection into Excel

**TIP**: Through the filters MedicalPortal the selection in the overview of the price matrix can be reduced or increased. The export download then takes the filters into account. For example: filter on items without an end date if you want to give these items an end date

4. Your browser downloads an Excel file
5. Change the desired fields in this file

**TIP**: The following fields are used to match the import with a record in the price matrix: declaration code, start date, stream, location, department, specialty. These may therefore not be changed in relation to the export/existing lines in the price matrix. With a bulk import the following data can be changed: end date, organization, organization group, Insurance package code, cost/price, invoice type, force administration, and VAT.

   - To change price matrix records, enter the mutation value ''2’’ in

6. Upload the file by dragging it into the appropriate field.
7. Click on Import prices to import the prices.
8. The system validates the rules in the import file and then modifies the prices.
9. Once the import is complete, a dialog box appears. This dialog box contains a "Continue to results" button. Clicking "Continue to results" opens a dialog box with an overview of both records with modified prices and non-imported modified prices. For the non-imported records, information is available explaining why the record wasn't imported. The adjusted price matrix rules will be immediately used by MedicalPortal.

---

<!-- chunk 40 | 90 tokens | part 1/1 -->
Manual section: Finance > Price matrix > Delete price matrix records > Single item

To delete prices (in bulk), you must do the following.

1. Go to Maintenance → Finance - Price matrix
2. Click on it trash icon of one price matrix record that you want to delete
3. Click on And the price matrix record has been removed and can no longer be used in MedicalPortal.

---

<!-- chunk 41 | 337 tokens | part 1/2 -->
Manual section: Finance > Price matrix > Delete price matrix records > In Bulk

1. Go to Maintenance → Finance - Price matrix
2. Apply filtering to the overview
3. Click at the top right Export prices
   1. Your browser downloads the filtered selection into Excel

**NB**: Through the filters MedicalPortal the selection in the overview of the price matrix can be reduced or increased. The export download then takes the filters into account.

*Example: Filter for items without an end date if you want to delete these items*

4. Your browser downloads an Excel file
5. To remove the prices, enter the mutation value “3”.
6. Upload the file by dragging it into the appropriate field
7. Click on Import prices to delete the prices
8. The system deletes the prices and no longer shows them in the overview
9. The system validates the records in the import file and then deletes the prices
10. Once the import is complete, a dialog box appears. This dialog box contains a "Continue to results" button. Clicking "Continue to results" opens a dialog box with an overview of both records with deleted prices and non-imported deleted prices. For the non-imported records, information is available explaining why the rule wasn't imported. The deleted price matrix records will immediately no longer be used by MedicalPortal

*Table: Format fields in Excel*

---

<!-- chunk 42 | 364 tokens | part 2/2 -->
Manual section: Finance > Price matrix > Delete price matrix records > In Bulk

| **Field** | **Description** | **Conditions** | **Example** |
| --- | --- | --- | --- |
| Declaration code | The declaration code | Declaration code must be present in the system | *15E934 is an existing declaration code in the system.* |
| Start date | Start date when rate for declaration code is active | dd-mm-yyyy | *01-01-2022* |
| End date | End date when rate for declaration code is active | dd-mm-yyyy | *31-12-2022* |
| Cost | The rate for the declaration code | Use a period (“.”) instead of a comma (“,”) if there are decimals. | *100.10 (Correct) 100,10 (Incorrect)* |
| Stream and Invoice type | Financial flow and invoice type | Selection list, fill in the selection list as stated | *NLDOT (Correct)*  *nl dot (Incorrect)*  *VECOZO (Correct)*  *Vecozo (Incorrect)* |
| Mutation | The code for the action required, such as new code, or changing or deleting an item | Only enter code 1, 2 or 3 | *1 (Correct)*  *1.0 (Incorrect)*  *12 (Incorrect)*  *1, (Incorrect)* |
| Organization, Organization group,  Insurance package code, Departments, Specialty, Location, Honorarium, VAT, force administration | Other text fields | Complete the fields exactly as stated by MedicalPortal.  Case sensitive | *If in MedicalPortal: Health Insurance North*  *In Excel: Health Insurance North (Correct)*  *health insurance north (Incorrect)*  *ZorgverzekeringNoord (Incorrect)* |

---

<!-- chunk 43 | 89 tokens | part 1/1 -->
Manual section: Finance > Ledger > General ledger matrix

In the ledger matrix can per administration, location, Departments, Cost Centers, Cost Bearers and financial flow indicate to which general ledger account number the costs should be posted. In this way, a distinction can be made between different cash flows in the (external) general ledger software.

---

<!-- chunk 44 | 138 tokens | part 1/1 -->
Manual section: Finance > Ledger > General ledger matrix > Add/change/delete general ledger matrix line

1. Go to Maintenance → Finance - Ledger matrix
2. Click on + Matrix
3. Fill in all desired fields. If any fields are missing from the drop-down list, this means that they have not (yet) been configured. Configure these fields on the appropriate Maintenance page and then try adding the ledger matrix line again.
4. Click on it pencil icon, if you want to change the administration
5. Click on it trash icon, if you want to delete the administration

---

<!-- chunk 45 | 79 tokens | part 1/1 -->
Manual section: Finance > Ledger > General ledger account numbers

Under general ledger account numbers you can configure which general ledger account numbers exist in the administration. This way the numbers can be included in the export MedicalPortal be related to the numbers known in the (external) ledger software.

---

<!-- chunk 46 | 118 tokens | part 1/1 -->
Manual section: Finance > Ledger > General ledger account numbers > Add/change/delete general ledger account number

1. Go to Maintenance → Finance - Ledger account numbers.
2. Click on + Account number
3. Enter name, number and description. Make sure that the number exactly matches the number known in the (external) ledger software.
4. Click on the pencil icon, if you want to change an account number.
5. Click on the trash icon, if you want to delete the administration.

---

<!-- chunk 47 | 124 tokens | part 1/1 -->
Manual section: Finance > Organization groups

The Netherlands has approximately ten groups that are directors for one or more labels and/or health insurers. It is possible that these labels and health insurers charge the same prices within the group. MedicalPortal offers the option to group these organizations into so-called Organization Groups. Entering prices in the price matrix can then be done at the level of the organizational group so that the price matrix is clearer and more compact.

---

<!-- chunk 48 | 201 tokens | part 1/1 -->
Manual section: Finance > Organization groups > Add/change/delete organization group

1. Go to Maintenance → Finance - Organization groups
2. Click on + Organization group
3. Enter name, Start and End Date (This indicates the validity of the organization group. See chapter Price matrix for which this period is used.
4. Enter invoicing from and Invoicing until (This indicates the period in which invoicing can take place)
5. Add organization group
   1. Click on + Linked organization (choose an organization entered in Maintenance -> Core - Organizations
6. Click on it pencil icon, if you want to change an Organization Group
7. Click on it trash icon, if you want to delete an Organization Group

When loading the price matrix, you can indicate to which organization group the entered price applies.

---

<!-- chunk 49 | 101 tokens | part 1/1 -->
Manual section: Finance > Exchange prices > Why set exchange prices?

Setting exchange prices is essential when dealing with international transactions or multi-currency payments. This ensures correct financial settlement, transparency for patients and you can respond to price changes. By setting an exchange rate, you can choose in which currency you want to create the invoice when creating an invoice.

---

<!-- chunk 50 | 126 tokens | part 1/1 -->
Manual section: Finance > Exchange prices > How to add an exchange rate?

Follow the steps below to add a new exchange rate:

1. Go to Maintenance → Finance - Currency exchange
2. Click at the top right + Currency
3. Fill in the required information for the currency
   Important: You enter the quantity of the exchange rate currency from a single unit of the base currency.
   See Exchange Rate image for an example:
   So 1.00 euro is 117.02 RSD on 06-01-2025

4. Click on Save

*Image - Exchange rate*

---

<!-- chunk 51 | 98 tokens | part 1/1 -->
Manual section: Finance > Exchange prices > Change or delete an exchange rate?

Follow the steps below to change or delete an existing administration:

1. Go to Maintenance → Finance - Currency Exchange
2. Go to the relevant exchange rate line with your cursor
3. Click on it pencil icon, if you want to change the exchange rate
4. Click on it trash icon, if you want to remove the exchange rate

---

<!-- chunk 52 | 54 tokens | part 1/1 -->
Manual section: Users & authorization > Users

Users are the people who have access to MedicalPortal. To access MedicalPortal, a user account must be created. To do this, go to Maintenance → User authorization - Users.

---

<!-- chunk 53 | 382 tokens | part 1/1 -->
Manual section: Users & authorization > Users > Create new user

1. Click at the top right + User.
2. Enter the following information:
   1. Username and email:
      1. The username is the name the user will use to log in.
      2. The user will receive an account activation link at the email address entered.

**NB:** Both the username and email address cannot be changed after saving.

   - First and last name
   - Phone number: this is used for 2 factor authentication (if not used, enter 0 here).
   - Groups: this determines which authorizations the user has. What authorizations exactly are and how they can be set is explained in the section Authorization groups.
   - Department and Specialty: in which Department(s) and in which specialty(s) the user works. Completing this helps the system pre-fill information for the user in various places.
   - Function: the function of the user. Based on this, the user can see notes sent to his/her function.
   - Status: If you set the user to Active, they will receive an email with a link to set a password.

**NB:** This link is only valid for 12 hours. If the user is set to Inactive, no email will be sent and the account cannot yet be used.

3. Click on Save.

**NB:** Share the username with the user. This username is not mentioned in the onboarding email that the user receives. As mentioned earlier, the user must set the password for the account within 12 hours.

4. After the user sets the password, the user can MedicalPortal open and log in with the new details.

---

<!-- chunk 54 | 150 tokens | part 1/1 -->
Manual section: Users & authorization > Users > Reset user password

If a user forgets his/her password, it is possible to reset it.

1. Go to Maintenance → User authorization - Users and look up the user.
2. Hover your mouse over the user and click on the pencil icon.
3. Click the button reset user password and click on yes when asked if you are sure.
4. The user will receive an email to reset the password.

**NB:** The user must change the password within 12 hours of receiving the email.

5. After the user changes the password, the user can MedicalPortal open and log in with the new details.

---

<!-- chunk 55 | 108 tokens | part 1/1 -->
Manual section: Users & authorization > Users > Change user

In addition to changing the password, it is also possible to reset other data.

1. Go to Maintenance → User authorization - Users and look up the user.
2. Hover your mouse over the user and click on the pencil icon.
3. Change the necessary data.
   **NB:** The username and email address cannot be changed afterwards.
4. Click on Save. The changes are immediately visible.

---

<!-- chunk 56 | 235 tokens | part 1/1 -->
Manual section: Users & authorization > Users > Delete user

1. Go to Maintenance → User authorization - Users and look up the user.
2. Hover your mouse over the user and click on the trash icon.
3. Click on And when asked if you are sure.
4. If desired, the user can then be created again. See step-by-step plan Create new user.

**NB:** Users who complete examination forms must be linked to a contact.

To do this, follow the following steps:

1. Create a user (as described in Create new user)
2. Create a Contact (as described in Contact book)
3. Add a working relationship to this contact
   1. Type Internal
   2. User = the user created in step 1
4. When creating a resource for this user, the contact from step 2 is also selected as the Executor.

These steps ensure that in various places MedicalPortal the executor is automatically selected when the user is logged in (for example as sender of a letter, or as creator of a recipe).

---

<!-- chunk 57 | 199 tokens | part 1/1 -->
Manual section: Users & authorization > Authorization groups

The authorization groups determine which users have which rights MedicalPortal. This is important because not all users are allowed to perform the same actions or view data. For this reason, it is often the case that the authorization groups are divided by function.

Authorization groups can be arranged according to a tree structure, with the child groups inheriting the rights of the parent groups. An example of a group structure is shown in *Image - Example of a group structure*:

*Image - Example of a group structure*

For example, when there is a new functionality MedicalPortal is added that must be available to all clinicians, the Clinician group can be assigned the right with which it is granted to all underlying groups.

---

<!-- chunk 58 | 487 tokens | part 1/1 -->
Manual section: Users & authorization > Authorization groups > Create authorization group

1. Go to Maintenance → User authorization - Authorization groups.
2. Click on + Group to create a new group.
3. Choose a name for the group and possibly a Parent to place the new group under an existing group.

**NB:** DThe group name must be unique.

4. Then choose for each component which rights this new group should have. The parts of MedicalPortal are split into different areas, under the 'Roles' section. When a role is in the 'Maintenance' group, this means that the role concerns the Maintenance of MedicalPortal. When a role is in the 'User' group, this means that the role is about the user side MedicalPortal.

For most parts MedicalPortal There are four types of rights:

* Create: the right to add a new item.
* Delete: the right to delete an item.
* Read: the right to view and look up an item in a table.
* Update: the right to modify an item.

A so-called 'Single' right applies to some items. This means that a user may or may not perform the actions. For example, printing a letter.

There are three options for each role:

* Yes: the action is allowed.
* No: the action is not allowed.
* Never: the action is never allowed, even if the same action is set to 'Yes' in a parent authorization group.

The overview of a group's rights shows what the effective right is. This is the applicable law for the group, taking into account the rights that apply in any parent groups.

**NB:** A 'yes' for a role somewhere in the tree structure is always stronger than a 'no'.

*Example: in the main group the permissions for creating a letter are set to Yes and in a subordinate group the same permissions are set to 'No'. Then the effective right for the underlying group is 'yes' because it is taken from the main group. If this is not desirable, the right in the underlying group can be set to 'never'. This rejects the 'yes' from the main group.*

---

<!-- chunk 59 | 145 tokens | part 1/1 -->
Manual section: Users & authorization > Authorization groups > Copy authorization groups

If you want to create a new authorization group that has the same rights as an existing group, it is possible to make a copy of the existing group. You can do this by following these steps:

1. Move your mouse over the existing group and click on its clone icon.
2. Give a new name to the group.
3. Click on Save. The group has now been created.
4. To then make changes to the group name, parent and/or permissions, you can hover over the group with your mouse and click on the pencil icon.

---

<!-- chunk 60 | 184 tokens | part 1/1 -->
Manual section: Medicine > Medication Maintenance > Recipe Maintenance

In this submenu of MedicalPortal all relevant medication Maintenance are configured. References are made to these institutions in the relevant chapters.

Prescription sending allows users to send a prescription directly to a pharmacist, patient or legal representative. Two configuration steps are required to send drafts.

Below Maintenance -> Medication - Medication Settings → Prescription Settings links a template from the notification templates to one of the three prescription recipients (pharmacy, patient, legal representative). The three possible prescription recipients are fixed and cannot be changed. It is possible to link one template to a recipient.

---

<!-- chunk 61 | 97 tokens | part 1/1 -->
Manual section: Medicine > Medication Maintenance > Recipe Maintenance > Recipe Maintenance - Link template to recipient

1. Go to Maintenance → Medication - Medication Settings → Prescription Settings
2. A template can be linked to a recipient under the heading Prescription Settings
   1. Click on it pencil icon
   2. Select an email template from the drop-down menu
   3. Click on Save

---

<!-- chunk 62 | 52 tokens | part 1/1 -->
Manual section: Medicine > Medication Maintenance > Recipe Maintenance > Adjust or delete recipe Maintenance

To edit a linked template, click on the pencil icon. To delete a linked template, use the trash icon.

---

<!-- chunk 63 | 57 tokens | part 1/1 -->
Manual section: Medicine > Medication Maintenance > Recipe Maintenance > Notification templates

A notification template for a recipe is created under notification templates. This template serves as the basis for a recipe email.

---

<!-- chunk 64 | 183 tokens | part 1/1 -->
Manual section: Medicine > Medication Maintenance > Recipe Maintenance > Add notification template

1. Go to Maintenance → Agenda - Notification templates
2. Click on + Template
3. Fill in the details (at least enter your name) → See Notification templates
   1. Select Recipe from the notification template category drop-down list
   2. Select Recipe from the Template Type drop-down list
   3. Select Email Trigger Secured or Not Secured

**NB:** When Email Trigger Not Secured is selected, recipe emails can also be sent non-securely. Because prescriptions contain confidential patient information, we strongly recommend that you select Email Trigger Secured. To set up secure email, see Maintenance → Core - Communication Settings.

---

<!-- chunk 65 | 57 tokens | part 1/1 -->
Manual section: Medicine > Medication Maintenance > Recipe Maintenance > Adjust or delete notification template

To customize a notification template, click on the pencil icon. To delete a notification template, use the trash icon.

---

<!-- chunk 66 | 36 tokens | part 1/1 -->
Manual section: Medicine > Log LSP

In this submenu of MedicalPortal all LSP queries are displayed. There is no option to do configuration here.

---

<!-- chunk 67 | 143 tokens | part 1/1 -->
Manual section: Medicine > P(C)MO > Why add a P(C)MO?

A predefined (combination) medication order (P(C)MO) allows the user to reuse a pre-filled saved medication order. This makes prescribing (commonly used) medication faster and easier.

A PMO concerns a single medicine for which a standard dosage and method of administration is specified. It is possible to add multiple PMOs of a specific medicine to offer different doses as PMO.

A PCMO is a combination of two or more PMOs. Existing PMOs are used to create a PCMO. The dosage is also taken over from existing PMOs.

---

<!-- chunk 68 | 95 tokens | part 1/1 -->
Manual section: Medicine > P(C)MO > How to add a PMO?

* Go to Maintenance → Medication - P(C)MO
* Click at the top right + PMO
  + Fill in the details (in any case medication, routeof administration, frequency, interval, amount, unit, name, specialty)
  + Click on Save

**NB:** The end user sees the specified name of the PMO in his/her overview and not the name of the medicine.

---

<!-- chunk 69 | 173 tokens | part 1/1 -->
Manual section: Medicine > P(C)MO > How to adjust/delete a PMO?

To adjust the PMO, click on the pencil icon. Here it is possible to modify or delete the existing PMO. It is not possible to delete a PMO if it is used in a PCMO.

To copy the PMO, click on the double squares icon. This creates a copy that can be edited immediately. This makes it possible to add a different dosage.

To deactivate a PMO, click on the cross icon. A deactivated PMO can be reactivated by means of its check mark icon.

**NB:** When you deactivate a PMO, any PCMO in which this PMO is used is also deactivated.

To delete a PMO, click on the trash icon. It is not possible to delete a PMO if it is used in a PCMO.

---

<!-- chunk 70 | 132 tokens | part 1/1 -->
Manual section: Medicine > P(C)MO > How to add a PCMO?

* Go to Maintenance → Medicine - P(C)MO
* Click at the top right + PCMO
  + Select the correct specialty (the specialty also serves as a filter for which PMOs are shown. It is not possible to assign PMOs from different Specialties to a PCMO.)
  + Select all medicines to add to the PCMO
  + Enter a name for the relevant PCMO
  + Click on save

**NB:** The end user sees the specified name of the PCMO in his/her overview, the added medicines are also visible in the subtext.

---

<!-- chunk 71 | 105 tokens | part 1/1 -->
Manual section: Medicine > P(C)MO > How to adjust/delete a PMO?

To adjust the PCMO, click on the pencil icon. Here it is possible to modify or delete the existing PCMO.

To copy the PCMO, click on the double squares icon. This creates a copy that can be edited immediately.

To deactivate a PMO, click on the cross icon. A deactivated PCMO can be reactivated by checking the box.

To delete a PMO, click on the trash icon.

---

<!-- chunk 72 | 170 tokens | part 1/1 -->
Manual section: Quality > Document Archiving System (DAS)

The DAS module allows users to save protocols in the electronic patient file. These protocols may relate to guidelines or work processes, but can also indicate how users should handle incidents or infections. Protocols have a title and a short description to give users an overview. Protocols can be created for multiple locations and Departments if they are general, but can also be created for one specific Departments. Categories are used to structure storage. Expiration date indicates the date until which a protocol is valid. Users can add up to 10 files to a protocol. Only PDF files of 20 MB or smaller can be added.

---

<!-- chunk 73 | 465 tokens | part 1/2 -->
Manual section: Quality > Document Archiving System (DAS) > Create and publish new protocol

Users can create and save a protocol with the status 'Draft' or send it immediately with the status 'New'. See image New DAS protocol for an example of the screen for creating new protocols. Once submitted with a status of 'New' it must be reviewed by another user. Others can approve or reopen it when changes are needed. Once a protocol has been approved, it can be published. A protocol remains published until it is archived. Archiving can be done manually or automatically.

1. Go to Maintenance → Quality - DAS
2. Click at the top right + Protocol.
3. Enter the following information:
   1. Protocol name
   2. Description: A brief description of the protocol for overview.
   3. Location: more than one location can be selected.
       *Example: Amsterdam and Utrecht*
   4. Departments: more than one Departments can be selected.
       *Example: Cardiology and Surgery*
   5. Category
   6. Subcategory
   7. Expiration date
4. Upload up to 10 files of up to 20 MB in size per file.
5. Then choose in which status the protocol will be saved.
6. Click on Send: the protocol is submitted and prepared for review.
   1. In addition Save as a concept is also an option: the protocol is saved as a draft and can be adjusted later.

The protocol must then be approved by a second user.

1. Click on Edit which appears when the cursor hovers over the protocol.
2. Click on Approve.
   Now the first user can continue publishing the protocol.
3. Click on Edit which appears when the cursor hovers over the protocol.
4. Click on Publish.

*Image - New DAS protocol*

Protocols always have an expiration date. A protocol can therefore pass its expiration date in all statuses. Whether a protocol has expired is visible in the overview page Maintenance → Quality - DAS.

---

<!-- chunk 74 | 100 tokens | part 2/2 -->
Manual section: Quality > Document Archiving System (DAS) > Create and publish new protocol

* Expired protocols that have not been published are marked orange on the left.
* Published protocols that have expired will have a red mark on the left.
* When the read-only version of an expired protocol is opened, a warning bar appears at the top of the protocol to indicate that the protocol has expired.

---

<!-- chunk 75 | 257 tokens | part 1/1 -->
Manual section: Quality > Document Archiving System (DAS) > Create a new version of a protocol

Users can create a new version of a protocol when a protocol is in Published or status Archived. This new version will be in a group together with the previous versions. Within this group, only one protocol can change the status “Published”. In the event that a new protocol is published, the group's existing Published protocol will automatically be transferred to Archived. The version history of the protocols in the group can be found under Edit → Medical protocol version.

**NB:** The groups are not shown on the page, but are only a convenience for explaining the functionality.

1. Go to Maintenance → Quality - DAS
2. Click on it plus icon which appears when the cursor hovers over the protocol
3. Change the information for the new version
4. Click on Send: the protocol is submitted and prepared for review
   1. In addition Save as a concept is also an option: the protocol is saved as a draft and can be adjusted later.

---

<!-- chunk 76 | 84 tokens | part 1/1 -->
Manual section: Quality > Document Archiving System (DAS) > Categories and subcategories

The protocols can be structured into categories and subcategories. These categories and subcategories can be created and modified. The screen in which this can be done and where all (sub)categories are listed looks like the image here on the right.

---

<!-- chunk 77 | 143 tokens | part 1/1 -->
Manual section: Quality > Document Archiving System (DAS) > Categories and subcategories > To add a category

1. Go to Maintenance → Quality - DAS
2. Click on it pencil icon next to the Category column name
3. Click on + Categories
   1. For categories
      1. Do not select Main Category
      2. Choose a name for the category
      3. Click on Save
   2. For subcategories
      1. Select a Main Category under which the subcategory should be placed
      2. Choose a name for the subcategory
      3. Click on Save
4. Then click Save in the Category Maintenance window

---

<!-- chunk 78 | 98 tokens | part 1/1 -->
Manual section: Quality > Document Archiving System (DAS) > Categories and subcategories > Change a category

1. Go to Maintenance → Quality - DAS
2. Click on it pencil icon next to the Category column name
3. Click on Change that appears when the cursor hovers over the category
4. Change the main category and/or name
5. Click on Save
6. Then click Save in the Category Maintenance window →

---

<!-- chunk 79 | 27 tokens | part 1/1 -->
Manual section: Quality > Reason for viewing log

In this submenu all registered reasons for access are shown.

---

<!-- chunk 80 | 217 tokens | part 1/1 -->
Manual section: Multimedia > Categories

It's in Maintenance → Multimedia - Categories possible to set which Multimedia categories are available in MedicalPortal. The multimedia categories follow a tree arrangement and are sorted in alphabetical order.

To add a new category, hover your mouse over an existing category and click on it plus the icon. The new category has been added as a 'child' of the existing category, with the name 'New category'. By hovering your mouse over the new category and clicking on the pencil icon you can change the name.

To delete a category, hover your mouse over the category and click on the trash icon and choose And. When documents have been placed in the category, these documents are moved to the category one level higher. So no documents are lost.

**NB:** It is only possible to delete categories that do not have a 'child'.

---

<!-- chunk 81 | 141 tokens | part 1/1 -->
Manual section: OpenEHR

When managing the forms you have to deal with 4 levels, which are visually depicted in the image below. From smallest to largest these are:

* Form fields (these are stored in the OPT library),
* Examination Segments,
* Examination Forms/functionalities and
* examination views

Each level is the building block for the next level. So: with form fields you build segments, with segments you build forms and with forms (and functionalities) you fill the examination views of Examination Types.

Image *- levels within one examination views*

---

<!-- chunk 82 | 106 tokens | part 1/1 -->
Manual section: OpenEHR > OPT library

The form fields are created by H4H, in a different system MedicalPortal. This is why OpenEHR is used, a method for standardization in the healthcare landscape. The fields are then uploaded into the 'OPT library’, this can be found in MedicalPortal under Maintenance → OpenEHR - OPT library. Loading these fields is done by H4H. You can then put the fields in this library into segments.

---

<!-- chunk 83 | 321 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Creating a new segment

Segments can be seen as building blocks of an Examination Form that consist of different fields. You can create a form by combining one or more segments.

* Go to Maintenance → OpenEHR - Examination Segments
* Click at the top right + Segment
* Enter the following information:
  + Category: You can assign the segment to a specific category. This can help make the segments clearer
    1. You can change or add a segment category on the left side of the page Examination Segments.
  + Maintenance name: the name of the segment that can only be seen on the maintenance side. This must be unique.
  + Display name: the name of the segment that (if set) is visible to the user in the form.
  + Type:
    1. Dynamic: When a segment is of type 'dynamic', fields can be placed anywhere in the segment with different sizes. This option provides the most flexibility and is chosen most often.
    2. Static: when a segment is of the 'static' type, fields can only be placed in a segment over the full width. This option is mainly used for questionnaires.

**NB:** The segment type cannot be changed after saving.

* Click on Save.
* To change the segment category or names, click on the pencil icon behind the segment.

---

<!-- chunk 84 | 312 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Segment designer

A segment is built by adding or changing fields to a segment. You can do this in the Segment designer.

1. Click on the second paper icon behind the relevant segment.
2. The segment overview page opens. Here you can see what the current version of the segment is and what any previous versions looked like
3. Click at the top right Edit segment content
4. Choose which form field you want to add in the segment. Clicking on the plus sign will add it
   1. Do you want to remove an added form field from the segment? Then click on the three dots in the field and choose 'Remove'
   2. Do you want to change an added form field? Then click on the three dots in the field and choose 'Edit'. Depending on the type of form field, you can make changes to the field here. For multiple choice fields, consider, for example, the order of answers, or the display of the field (list selection or radio buttons). For more information see Segment Maintenance
   3. By pulling the arrow of a form field in or out you can make the field larger or smaller. It is also possible to drag the fields within the segment to determine the location and order
5. Click on Publish when the segment is finished.

---

<!-- chunk 85 | 106 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Maintenance per field

You can change various Maintenance per form fields within a segment. The options depend on the type of field. You can see which type a field is next to the field name when you are in the segment designer. The most common field types are: Select, Text, Date and Text with select. These field types and the possible options will be further explained below.

---

<!-- chunk 86 | 485 tokens | part 1/2 -->
Manual section: OpenEHR > Examination Segments > Maintenance per field > Select

The fields of the type 'select' are multiple choice fields.

* Hidden: set this to Yes if the field should only become visible if a certain condition is met (see explanation below under 'Add dependencies'). With option No, the field is always visible
* Require this field: if you select Always, you will not be able to save the form before completing this field
* Help text: this is the text that appears when you hover your mouse over the i next to the field name
* Input type: the shape of the field in the form
  + Radio buttons: the answer options are visible in the form with a round button and only 1 answer can be chosen
    - If a question is optional, a cross will be available in the form
  + Select from a list: the well-known drop-down list in which the user can choose one or more answers
    - When multiple answers are allowed, the 'Select all' option is also an option in the form
  + Check boxes: the answer options are visible in the form and multiple answers can be chosen by checking the boxes
    - Only for questions with multiple answer options
* Input layout (in case of Radio Buttons or Check Boxes input type)
  + A column: the answer options are presented in a column
  + Side by Side: The answer options are presented on one line
* Order of Answers: The order of the answer options. You can drag this
* Available Answers: Provides the option to leave a specific answer unavailable as an option
* Standard answer: gives the option to choose an answer as a standard answer.

**NB:** This option is always selected for mandatory questions

**NB:** Dit means that this field and the segment will always be shown in the letter

* Placeholder: This text appears in the empty form field (until the user enters or selects an answer)
* Label: Change the name of the field if desired
* Dependency: Allows you to set a dependency between fields.

---

<!-- chunk 87 | 72 tokens | part 2/2 -->
Manual section: OpenEHR > Examination Segments > Maintenance per field > Select

*Example: question 2 only appears if you answer 'A' to question 1. You set the dependency at 'question 1': If 'question 1' = 'answer A', then 'show' 'question 2'. At 'question 2' set the Hidden option to Yes.*

---

<!-- chunk 88 | 210 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Maintenance per field > Text

Fields of the type 'text' are free text fields.

* Hidden: set this to Yes if the field should only become visible if a certain condition is met (see explanation below under 'Add dependencies'). With option No, the field is always visible
* This field is required: if you select Always, you will not be able to save the form before completing this field
* Help text: this is the text that appears when you hover your mouse over the i next to the field name
* Text box type:
  + Single Line: A single line of text is allowed in the text box
  + Multiple Lines: Multiple lines of text are allowed in the text box
* Placeholder: This text appears in the empty form field (until the user enters or selects an answer)
* Label: Change the name of the field if desired

---

<!-- chunk 89 | 215 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Maintenance per field > Date

Fields of the type 'date' are date fields.

* Hidden: set this to Yes if the field should only become visible if a certain condition is met (see explanation below under 'Add dependencies'). With option No, the field is always visible
* Require this field: if you select Always, you will not be able to save the form before completing this field
* Help text: this is the text that appears when you hover your mouse over the i next to the field name
* Input type: the shape of the field in the form
  + Date Picker: Full: The user can only select a full date
  + Date Picker: Partial: The user can select a complete or incomplete date
* Placeholder: This text appears in the empty form field (until the user enters or selects an answer)
* Label: Change the name of the field if desired

---

<!-- chunk 90 | 492 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Maintenance per field > Text with select

Fields of the 'Text with select' type consist of two parts; a part where you enter a numerical or textual value and a part where you can select a value (a unit).

* Default unit: allows you to choose a default unit for the answer. Also provides the option to allow only the selected default unit
* Range from-to: gives the option to enter the allowed minimum and maximum value of the answer
* Hidden: set this to Yes if the field should only become visible if a certain condition is met (see explanation below under 'Add dependencies'). With option No, the field is always visible
* Require this field: if you select Always, you will not be able to save the form before completing this field
* Help text: this is the text that appears when you hover your mouse over the i next to the field name
* Calculation: you can select a matching calculation here. When the requirements of the calculation are met, the result of the calculation will appear in this field

**NB:** THEIn order for the calculation to run properly, it is important that the fields that belong to the calculation are all in the segment and that the user has filled them in

*Example: to create the BMI calculation, the Height and Weight fields must be filled in by the user and the BMI calculation must be selected on a field (for example the 'BMI' field) in management*

* + The calculation requirements are set by H4H. So you cannot make any changes here, or add or remove a calculation
* Placeholder: This text appears in the empty form field (until the user enters or selects an answer)
* Label: Change the name of the field if desired
* Dependency: Allows you to set a dependency between fields

*Example: question 2 only appears if you answer 'A' to question 1. You set the dependency at 'question 1': If 'question 1' = 'answer A', then 'show' 'question 2'. At 'question 2' set the Hidden option to Yes.*

---

<!-- chunk 91 | 487 tokens | part 1/2 -->
Manual section: OpenEHR > Examination Segments > Examination segments

Examination segments is the display of all completed fields within a segment on the timeline and/or in a letter. By setting this, the research results become more readable. To set up this summary, click on the third edit icon behind the relevant segment (see Image - Change segment summary).

*Image - Change Examination segments*

The image below gives you a list of all fields of the segment. In this screen you can make the following changes:

* Field order: you can change the order of the fields by dragging the fields at the three lines
* Text Before: Here you can type text that will appear before the entered value of the field. It is also possible to apply styling to the text, such as bold. You can do this by selecting text and choosing the desired formatting from the formatting options

**NB:** INif the field has no value, the text before and/or text after will not be displayed in the letter or on the timeline

* Text After: Here you can type text that will appear after the entered value of the field. It is also possible to apply styling to the text, such as bold
* Properties: properties that you can give to this specific field within a segment:
  + Exclude from letter: when this value is checked, this field will not be included in the Examination segments in the letter

**NB:** To get an examination segment in a letter, a letter item must first be added to the letter template. How exactly this should be done is further explained in the chapter 'Correspondence'

* + Exclude from timeline: When this value is chosen, this field will not be included in the Examination segments on the timeline
  + New Line: When this value is chosen, the line of the corresponding field within the segment will start on a new line
  + Exclude unit: when this value is chosen and the corresponding field has a unit, this unit will not be shown in the Examination segments

---

<!-- chunk 92 | 92 tokens | part 2/2 -->
Manual section: OpenEHR > Examination Segments > Examination segments

The changes you make here will not affect the fields in the segment itself. By looking at the 'Example timeline' and 'Example letter' screens within changing the Examination segments, you can see how the current version of the Examination segments will be reflected in the letter and on the timeline.

---

<!-- chunk 93 | 100 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Segments > Examination segments > Other functionalities

On the page with the segments, there are three more buttons behind the action buttons we just discussed:

* Through it list icon you can see in which forms the segment is used
* With it copy icon you can copy the segment
* Through it clock icon you can view the change logs

*Image - Of Examination segments*

---

<!-- chunk 94 | 384 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Forms > Create a new form

You can compile Examination Forms by combining them. Examination forms can be used in two places: within a study, or as a questionnaire.

1. Go to Maintenance → OpenEHR - Examination Forms
2. Click at the top right + Form
   1. The functionality 'Import form' is used for standard forms; in practice you will rarely or never use this after the initial setup
3. Give the form a (unique) management name, a display name (visible to the user) and a description and click Save
4. As with segments, you can change the form's management and display name by clicking the pencil icon in the line of the form on the right side.
5. Click on the paper icon in the same line you just created.
6. The form overview page opens. Here you can see what the current version of the form is and what any previous versions looked like
7. Then click at the top right Edit form content to edit the form
8. In the next screen you can add the desired segments to the form

**NB:** Can't find a segment? Then you probably haven't finished the segment and clicked Publish yet.

9. You can then change the size of the segments by pulling the segment arrow in or out, or change the order of segments by dragging them. It is also possible to use the 3 dots to set whether the name of the segment should be displayed in the form
10. When you're done, click Save or Publish. When you choose Save, the new version of the form will not yet be available to users. If you choose Publish, this will be the case

---

<!-- chunk 95 | 71 tokens | part 1/1 -->
Manual section: OpenEHR > Examination Forms > Create a new form > Other functionalities

* With the copy icon you can copy the segment
* Through it clock icon you can view the change logs
* Through it export icon you can export the form and then import it again in another environment

---

<!-- chunk 96 | 135 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views

One of the places where you can use your created forms is in a study. You can set this via an examination view. Immediately examination views focus on what the user sees when opening a survey. The set study views within a study are shown in the column on the left. In addition, on this page you have the option to add an ORU mapping. This allows you to independently map HL7 messages, type ORU, on examination views, so that results (e.g. from an external ECG device) end up in the correct field.

---

<!-- chunk 97 | 188 tokens | part 1/2 -->
Manual section: OpenEHR > Examination views > A new one examination views to make

1. Go to Maintenance → OpenEHR - examination views.
2. Find the study you want to set up a view for and click on the pencil icon.
   1. Do you still need to create the survey? How to do this is described in the chapter Examination Types.
3. You are now in the overview screen of this study. This contains all examination views and templates
   1. Views (red in the image examination views): Here you can find all examination views for this study
   2. Timeline (yellow in the examination views image): the timeline for the selected examination views
   3. Templates (blue in the Set Study View image): the set templates for this study

*Image - The examination views set*

---

<!-- chunk 98 | 416 tokens | part 2/2 -->
Manual section: OpenEHR > Examination views > A new one examination views to make

4. Click on + View to add an examination view.
5. Give the examination views a name and click Save. The view has now been added, but has no content yet.
6. By clicking the newly added view or the pencil icon clicking, you can add the timeline on the right side (yellow in the image above). This way you can also change the timeline of already existing views:
   1. Name: the name of the examination views.
   2. Hidden: set this to Yes if the view should only become visible if a certain condition is met (see explanation below under 'Add dependency'). With option No the display is always visible.
   3. Forms: select the form you want to display in the examination view.
      1. Can't find the form? Then you probably still have to publish these within 'Examination forms'.
      2. When a form is selected, the option 'Pre-filling from previous appointment allowed' will appear. When this is checked, the user is able to import the values into the form into the appointment if they have already been entered in a previous appointment.
   4. Functionalities: select the functionality that you want in the examination views. Most functionalities cover the entire screen, except the timeline, PDF viewer and Appointment questionnaire. With the last three you can display a form and functionality at the same time. This is not possible with the other options
7. After adding a form and/or functionality, click the examination views always up Save on the right before moving on to the next view

**TIP:** Via the button Example you can see a preview of the styled views from this study

---

<!-- chunk 99 | 79 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Setting up a link

At the heading 'Add link to view' you can make a reference to a DAS file and/or an external link within a study, so that the user can easily open it. You can by examination views set multiple links. These will be displayed as a button within a survey.

---

<!-- chunk 100 | 240 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Set up dependent examination views

It is possible to cancel the screening of an examination view to make it dependent on an answer entered in a form from another view. (Nog doen)

*Example: In the 'Symptoms' form, 'Chest pain' and 'Dyspnea' are checked. Now two new forms for querying these symptoms will appear for the user on the left.*

To set up a dependent view:

1. Set the view to appear when the dependency is met. Choose 'Hidden' as Yes.
2. Click on the view that contains the trigger for the dependent view to appear.

**NB:** It is only possible to set a view as a trigger when a form is linked to this view.

3. Set under the heading 'Dependency' the dependency.

*Example: If symptom = chest pain, then tone examination views “Chest pain.” Now when the user opens the survey, the examination views 'Chest pain' not immediately visible. This is only available when chest pain is selected as the symptom.*

---

<!-- chunk 101 | 199 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Set of research display templates

For one examination view, setting up a template, for example with normal values, can make it easier for the user to complete one or more Examination forms. It is possible to create a template for a single one examination view, but also for several at once.

To set up a survey view template:

1. Click on the button + Template
2. Give the template a name and a description. The name is the text that will appear on the button within the study
3. Enter the desired values in the template and click Save

When the user then opens the relevant study, a button will appear at the top of the form, for example 'Normal ECG'. If the user clicks on this, the forms of the relevant study will be filled with the preset values.

---

<!-- chunk 102 | 110 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Maps of HL7 ORU messages

In MedicalPortal you have the option to map ORU messages yourself on examination views. This links the result fields of incoming HL7 messages, type ORU, to the fields in an examination view. When this type of message is received in the future, the results will end up in the right place in the research. (Read more about HL7 and ORU messages in the chapter HL7 Messages)

---

<!-- chunk 103 | 219 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Maps of HL7 ORU messages > Adding a mapping of an ORU message

1. Go to Maintenance → OpenEHR - examination views.
2. Open the examination views for which you want to add a mapping.
3. Click on + ORU mapping, a new screen will now open.
4. Add an ORU message to the text box.
5. Click on Following.
6. Add per field from the examination views the correct value from the ORU message.
   1. Values from the ORU message can only appear once. Once a value has been chosen, it is not possible to add it again to another field from the examination view.
7. Adjust the unit if necessary.

**NB:** Not all units can be adjusted. If you want to convert a unit but the correct option is not available. Please consult the Heart for Health service desk.

8. Click on Save.
9. The mapping has now been added and visible in the examination views.

---

<!-- chunk 104 | 139 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Maps of HL7 ORU messages > Adjusting or removing a mapping

If an ORU mapping needs to be adjusted or deleted, this can be done via the button ORU mapping. Here it is possible to adjust or delete a mapping. Adjusting the message is based on the initially loaded message. It is possible to load a new ORU message. To do this, go to the tab Customize message. Then press the button Update.

**NB:** When updating the message, the mapping of all fields that do not appear in the old and new ORU message is removed.

---

<!-- chunk 105 | 118 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Asynchronous examinations

It is also possible to set up examinations to be processed in an asynchronous manner. These are examinations with a first and second appointment (e.g. Holter and 24hr bpm). When asynchronous examinations are set up correctly, it is possible for users to link created orders from a first appointment to the second appointment. This allows results to be automatically loaded into the second appointment.

---

<!-- chunk 106 | 116 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Asynchronous examinations > Asynchronous examination configuration

Before a user can link asynchronous orders, you will need to set up the asynchronous examinations. The asynchronous examinations only work for the Holter and 24h blood pressure examination types. In addition, examinations should be set with process asynchronous, with one examination indicated as the first examination and one as the second examination.

---

<!-- chunk 107 | 232 tokens | part 1/1 -->
Manual section: OpenEHR > Examination views > Asynchronous examinations > Asynchronous examination configuration > Configuration of first and second examination

To set up examinations as asynchronous you go to Settings → Examination views → *select the correct examination* → Design form

In the examination you select the top view and look at the settings. These are set as follows:

* Functionalities is PDF viewer
* Type is Order
* Order type is Holter or 24h bloodpressure
* Order receiver is *free to fill out*
* Process is a-synchronized

To make it possible to link orders in an asynchronous examination, one of the two examinations must be marked as the first examination and another examination as the second examination. You can fill in the remaining fields as you wish, for example, what form you want to display and whether or not you want to display the PDF viewer. The asynchronous orders can now be linked by users.

---

<!-- chunk 108 | 226 tokens | part 1/1 -->
Manual section: OpenEHR > Letter Templates

Letter templates help standardize and automate correspondence with MedicalPortal. They are used as the basis of all outgoing correspondence, except for appointment confirmations and reminders. A letter template is the preset design and content of, for example, report letters for the referrer or the patient. This letter template consists of plain text, variables and letter items.

* You can add plain text yourself and it will appear exactly as it appears in every letter you create.
* Variables contain preset information in a letter that you cannot modify.

*Example: Appointment type or Patient*

* Letter Items can be customized by you by adding components from different studies to a brief item. You can compare this with a chapter in which you add the paragraphs yourself.

**NB:** Letter items are only used for information from appointment inquiries.

---

<!-- chunk 109 | 196 tokens | part 1/1 -->
Manual section: OpenEHR > Letter Items

Letter items are the configurable building blocks of a letter template. These in turn consist of Examination Segments. A summary of these Examination Segments, the segment summary, determines the content of the letter ((see chapter Formulate for further explanation). Letter Items can contain multiple survey segments, as shown in the example given in the image to the right.

1. Go to Maintenance → OpenEHR - Letter Items
2. Click at the top right + Letter item
3. Enter the following information:
   1. Name: this name will be displayed in the letter
   2. Description
4. Then add the desired Examination Segments whose segment summary you want to display in the letter item
   1. Adjust the order of the segments if necessary
5. Click on Save

---

<!-- chunk 110 | 513 tokens | part 1/1 -->
Manual section: OpenEHR > Letter Items > Create a letter template

Letter templates act as preset formats for letters. These templates contain many options for letter presets, which are briefly described in step 3 of the step-by-step plan below this paragraph. The template also determines the design of the letter content, which can consist of plain text, letter items and variables. In image create a letter template is an example of the window for creating a letter template. This shows how the content selection works, with a combination of letter items, variables, plain text and fields.

1. Go to Maintenance → OpenEHR - Letter templates
2. Click at the top right + Template
3. Enter the following information:
   1. Name
   2. Default recipient: this automatically prefills the 'Recipient' field when sending the letter.
       *Example: Set the patient as the default recipient.*
   3. Default CC: this automatically prefills the 'CC' field when sending the letter.
       *Example: Set the GP as the default CC.*
   4. Subject: the subject of the letter or email.
   5. Mail trigger: this determines whether the letter is sent only securely or whether unsecured sending is also allowed.
      1. Secure emailing depends on the Communication Settings (see chapter Communication Settings). If no Communication Settings are configured, a secure letter cannot be sent.
   6. Category: the category in which the letter template is placed
   7. Status: inactive templates are not shown at the step select template for a letter, active templates are
   8. Margins: these are especially important if you are going to print the letter.
4. Then fill the template with text, letter items and variables.
5. Click on Save

*Image X - Create a letter template*

Letter templates can then be linked to Appointment types (see chapter Agenda). It is also possible to manually select a letter template when sending the correspondence. The content of the letter, including the design of the template, can then also be manually adjusted before sending the letter.

---

<!-- chunk 111 | 64 tokens | part 1/1 -->
Manual section: Patient > Allergies

Allergies registered by the patient can be classified into two allergy types: Medication and General. On the allergies configuration page, add allergies that are selectable for the end user under the General allergy type.

---

<!-- chunk 112 | 90 tokens | part 1/1 -->
Manual section: Patient > Allergies > Allergy type medication

When chosen by the end user For allergy type medication it is possible to choose a medicine/group/substance name/substance name\_route of administration based on the Z-index. When prescribing medication, a warning will then appear if the patient is allergic. No configuration is required for this.

---

<!-- chunk 113 | 161 tokens | part 1/1 -->
Manual section: Patient > Allergies > General allergy type > How to add an allergy?

The list of allergies offered under allergy type general can be maintained in the Allergies table.

1. Go to Maintenance → Patient - Allergies
2. Click at the top right + Allergy
3. Fill in the details (at least Name and Category and Start Date).
4. Click on Save

It is advisable to add a SNOMED CT code when entering an allergy. This code promotes standardized recording and exchange of data.

Do you want to add multiple allergies at once? This is faster via the button Import allergies.
Here you can download a sample file, complete it and import it again.

---

<!-- chunk 114 | 90 tokens | part 1/1 -->
Manual section: Patient > Allergies > General allergy type > How to change an allergy?

You can change an allergy by clicking on the pencil icon behind the allergy.

It is possible to archive an allergy if it can no longer be registered. This can be done by specifying an end date. Allergies that have already been registered with a patient always remain visible.

---

<!-- chunk 115 | 61 tokens | part 1/1 -->
Manual section: Patient > Allergies > General allergy type > How to remove an allergy?

Removing an allergy is only possible if it is not registered with a patient. Click on the trash can icon behind the allergy to permanently delete an allergy.

---

<!-- chunk 116 | 302 tokens | part 1/1 -->
Manual section: Patient > Diagnoses

Diagnoses must be set to add standardized information to the patient record and for correct financial settlement. To facilitate this, a diagnosis contains a number of fixed components:

* Name (the diagnosis in question)
* DBC code (for financial settlement)
* ICD10 code (for exchange with other healthcare providers and financial settlement).
* Specialty (for which specialty the diagnosis can be selected)
* Start date (date from which the diagnosis can be selected)
* End date (date from which the diagnosis can no longer be selected)

A diagnosis also contains some additional components:

* Synonym(s) (other terms that can be used for diagnosis)
* Description (additional information; this is not visible to the user)
* SNOMED code (for exchange with other healthcare providers)
* Parent diagnosis (if a diagnosis is a specification of a 'parent diagnosis'

*Example: 'Acute heart failure based on arrhythmia' is a 'child diagnosis' of 'Acute heart failure', the 'parent diagnosis')*

Diagnoses can be added manually (individually or in bulk). MedicalPortal. MedicalPortal also supports the use of the Diagnostic Thesaurus. Below is an explanation for both options.

---

<!-- chunk 117 | 140 tokens | part 1/1 -->
Manual section: Patient > Diagnoses > Add diagnostics manually

1. Go to Maintenance → Patient - Diagnoses
2. Click “+” at the top right Diagnosis

* Do you want to add a large number of diagnoses at once? This is faster via the button *Import diagnoses.* Here you can download a sample file, complete it and import it again.

3. Fill in the details (at least Name and Specialty)

NB: it is important to also add a DBC and ICD10 code if the diagnosis(es) is/are used for financial settlement. That is without this information **not** possible.

4. Click on Save

---

<!-- chunk 118 | 123 tokens | part 1/1 -->
Manual section: Patient > Patient overview

The patient overview is used to show a current image of a patient at a glance. Most of the patient overview is configured by default. One card on the patient overview can be configured via the Maintenance page to show specific information, namely OPT fields from the forms (for more information about the operation of OPT fields see chapter Formulate). For an optimal user experience, we recommend configuring the latest discussion and policies here.

---

<!-- chunk 119 | 199 tokens | part 1/1 -->
Manual section: Patient > Patient overview > Configure sections

1. Go to Maintenance → Patient - Patient overview.
2. Click on it pencil icon to change the name of the card on the patient overview.
3. Click on + Section # to add a section.
   1. Selectable sections are fields from the OPT library.
   2. When a field is selected it is shown on the patient overview. The field is shown as it was filled in for the most recent appointment. If the field is not filled in, older appointments will be checked to see whether the field has been filled in and the most recent will be shown. If nothing is entered, nothing will be shown.
   3. By adjusting the display name, the displayed name of the field on the patient overview is adjusted.
   4. Click on save.
4. A maximum of 3 sections can be shown.

---

<!-- chunk 120 | 48 tokens | part 1/1 -->
Manual section: Patient > Patient overview > Customize sections

To customize a section, click on the pencil icon at the section. It is possible to select a new field or change the display name.

---

<!-- chunk 121 | 59 tokens | part 1/1 -->
Manual section: Patient > Patient overview > Delete sections

To delete a section, click on the trash icon. Deleting a section ensures that it is no longer shown on the patient overview. After deleting it is possible to add a new section.

---

<!-- chunk 122 | 237 tokens | part 1/1 -->
Manual section: Patient > Wristband and sticker templates

It is possible to print a wristband or sticker from the patient file. To do this, you must first have set up templates MedicalPortal.

Adding a wristband or sticker template works as follows:

1. Go to: Maintenance → Patient - Wristbands & Stickers
2. Click on + Wristband or + Sticker Fill in the following fields:
   1. Name
   2. Width (cm)
      Enter the width of the stickers/wristbands you use here.
   3. Height (cm)
      Enter the height of the stickers/wristbands you use here.
   4. Marge (cm)
      This is the space from the edge of the sticker/wristband where no text is printed.
   5. Start and end date: the period in which the template is available.
3. You can then add the desired content to your template by selecting variables and/or adding free text.

You can remove a sticker/wristband template by pressing the pencil icon clicking behind the template to be deleted.

---

<!-- chunk 123 | 94 tokens | part 1/1 -->
Manual section: Patient > Questionnaires

Questionnaires allow patients to answer questions about their medical situation in their own time and allow the user to go through them at a convenient time. This chapter discusses the use of questionnaires within MedicalPortal explained. The following aspects will be explained:

* Management and Maintenance
* Types of questionnaires

---

<!-- chunk 124 | 449 tokens | part 1/1 -->
Manual section: Patient > Questionnaires > Management and Maintenance

To create a questionnaire, the same steps must be completed as described in the Chapter Forms. Once a form has been created, it can be selected and added as a questionnaire.

**TIP:** By giving the segment in the questionnaire type 'Static' and sorting the questions vertically, the questions will always be presented to the patient in the correct order.

Creating a questionnaire is done as follows:

1. Create the desired form, as described in the Chapter Forms.
2. Go to Maintenance → Patient - Questionnaires.
3. Click on + Questionnaire.
4. Fill in the following fields:
   1. Name: the name of the questionnaire. This is visible to both the user and the patient.
   2. Short instructions: here you can place any short instructions for the patient.
   3. Form: here you can select 1 form that will serve as the content of the questionnaire. Rules associated with a field (dependencies, mandatory) are also included in the questionnaire.

**NB:** When you make changes to this form, or any of the segments in this form, these changes will also be automatically reflected in the questionnaire.

   - Add to infection check: when you check this option, the questionnaire will be available as an option as an infection check on the patient page.
   - Status: give the questionnaire a status. When the questionnaire has a status of Active, it is available to be used. This is not the case with the status Archived.
   - **Please note**: A validation check is performed on questionnaires.
     A validation check is performed when creating or modifying a questionnaire. This is to prevent identical questionnaires. It is possible to have only one active questionnaire per form.

5. Choose Save. The questionnaire is ready to use!

---

<!-- chunk 125 | 197 tokens | part 1/1 -->
Manual section: Patient > Questionnaires > Types of questionnaires > Appointment questionnaires

There are in MedicalPortal Two types of questionnaires are possible: appointment questionnaires and manual questionnaires.

An appointment questionnaire is a questionnaire that is linked to an appointment. Users can manage one questionnaire and link it to an appointment. You can do this by entering an appointment type in the field when changing or creating an appointment type Questionnaires select a questionnaire. If this appointment is subsequently scheduled, the patient will receive an invitation to log in to the app and complete the questionnaire. The patient can then complete the questionnaire in the app. The answers are finally sent to MedicalPortal, where the user can view them.

---

<!-- chunk 126 | 343 tokens | part 1/1 -->
Manual section: Patient > Questionnaires > Types of questionnaires > Questionnaire examination views

If a questionnaire is linked to an appointment, it is also useful if the user can view the answers from the questionnaire within this appointment. To enable this, this must be configured within a examination views:

1. View which Examination Types are included in the appointment and decide in which Examination Types it is useful to view the questionnaire. There can also be several if desired.
2. Enter Maintenance → OpenEHR - Examination Views to the desired Examination Types.
3. Click on the pencil icon.
4. Click on an already existing one examination view, or create one. How to do this is explained in the chapter examination views.
5. Choose as a functionality Appointment questionnaire.
6. If you also choose the questionnaire form as a form, this form and the questionnaire answers are visible to the user side by side. In this way it is possible for the user to use the functionality Copy data to be used when completing the form.

*Example: for the New Patient appointment type, the Social History questionnaire is selected. When this appointment is scheduled, the patient can complete his/her social history before the appointment. The user can then view the results of the questionnaire within the appointment and, if necessary, import them into the form.*

---

<!-- chunk 127 | 102 tokens | part 1/1 -->
Manual section: Patient > Questionnaires > Types of questionnaires > Manual questionnaires

The second type of questionnaires MedicalPortal are Manual questionnaires. The user can send these questionnaires to the patient without an appointment. The only configuration required to send manual questionnaires is to create a questionnaire. How to do this is described under the heading Management and Maintenance.

---

<!-- chunk 128 | 113 tokens | part 1/1 -->
Manual section: Resource

Agreements with associated studies form the base of MedicalPortal. An appointment always consists of one or more examinations.

*Example: When a new patient comes to the consultation hour, a medication check, an intake, a lab test and a consultation are carried out. To do this, you set up an appointment type 'New patient', which consists of the Examination Types 'Medication check', 'Intake', 'Lab examination' and 'Consult'.*

---

<!-- chunk 129 | 249 tokens | part 1/2 -->
Manual section: Resource > Examination Types

A resource type and possibly the financial registration are linked to the investigations within an appointment. Once you have added an Examination Type, it is possible to also add an examination view in which forms and other file information are then displayed.
**TIP:** A survey can be used in multiple appointment types. Only if appointment types require that the examinations on the data below (points 3-6) differ from each other is it necessary to create multiple examinations, or when a different examination view is desired.

*Example: an ECG examination takes 5 minutes and is normally performed by a nurse. However, at a certain appointment the ECG must be performed by a specialist and lasts for an hour of 10 minutes. In this case, a separate survey must be created to include in the relevant appointment. The other data (registration code, specialty, etc.) can be the same as the 5-minute examination.*

You can add a survey type as follows:

---

<!-- chunk 130 | 463 tokens | part 2/2 -->
Manual section: Resource > Examination Types

1. Go to Maintenance → Agenda - Examination Types
2. Click on + Examination Types
3. Enter the following information
   1. Used in
      Here you can choose whether you want to use this Examination Types in appointments or recordings. It is not possible to select both appointments and recordings or to change this afterwards.
      **NB:** This is part of the Admissions module in which bed planning is possible. This module may not be available to you. When recording study types are added, they will appear on a second tab: Recordings.
   2. Name: shown to the user in the calendar and in the appointment.
   3. Code: Shown to the user in the survey.
   4. Description
   5. Specialty
      See Specialty for configuring Specialty.
   6. Default resource type: this resource type and resources of this resource type are pre-selected when scheduling an appointment. It is possible to change the resource type when scheduling an appointment or from the scheduled appointment.
   7. Start and end dates: period during which the survey type is available to add to an appointment type.
   8. Duration (in min)
4. Can a survey only be performed by one resource type? Then tick 'Allow only default resource type ' On. The resource type cannot then be changed when creating the appointment or from a scheduled appointment.
5. Double approval: If you check this box, the study must be approved by a second person (in most cases a doctor) after completion before the study is given the Done status.
6. You can add a registration code to the survey type by clicking + Registration code. Then enter the registration code, start date and possibly an end date and click Save. The registration code forms the base of the healthcare registration (Financial activity) that is created after the research has been completed.

---

<!-- chunk 131 | 103 tokens | part 1/1 -->
Manual section: Resource > Appointment types

Appointment types consist of one or more investigations and are always linked to at least one Department. The appointment confirmation/reminder, a letter template and the invoicing method are also linked to the appointment type. Before you can set up an appointment type, at least one Departments, An letter template and one Examination Type are set in MedicalPortal.

---

<!-- chunk 132 | 161 tokens | part 1/1 -->
Manual section: Resource > Appointment types > Financial handling

A financial activity is created when a linked inquiry, with a set registration code, has been completed. A financial activity is also created when an appointment, with a registration code set using the Package Registration Codes field, is completed. You can add a registration code to the appointment type by clicking + Registration Code. Then enter the registration code, start date and possibly an end date and click Save. The financial activities contain data from chapter Financial information and from the referrer of the appointment and the person conducting the research.

---

<!-- chunk 133 | 502 tokens | part 1/3 -->
Manual section: Resource > Appointment types > Financial handling > How to add an appointment type?

Creating an appointment type works as follows:

1. Go to Maintenance → Agenda - Appointments
2. Click at the top right + Appointment
3. In the screen that appears you will see the following fields:

*Table: Appointment type fields*

| **Field** | **Explanation** |
| --- | --- |
| **General Maintenance** | |
| Code | The code under which an appointment type is known within your organization. This code does not appear in communication with patients. |
| Name | The name of the appointment is stated in several places MedicalPortal shown, such as during scheduling the appointment and in the agenda. |
| Description | Will be shown in the appointment confirmation. |
| The Departments | This is the Departments where the appointment type is available and therefore for which Departments the appointment can be booked. It is possible to select multiple Departments. |
| Start date | The date from which an appointment is available to be scheduled |
| End date | The date until which an appointment is available to be scheduled |
| Default referrer | The default referrer of an appointment type. See Standard referrer for further explanation. |
| **Notifications** | |
| Appointment confirmation | Appointment confirmations will be sent once the appointment is scheduled. See Notification templates for instructions on setting up notification templates. A maximum of one general template, one location-specific template and one Departments-specific template can be linked per appointment type (see Levels of notification templates). |
| Reminder | Appointment reminders are emailed a few days before the appointment. See Notification templates for instructions on setting up notification templates. A maximum of one general template, one location-specific template and one Departments-specific template can be linked per appointment type (see Levels of notification templates). |
| **Financial Settings** | |

---

<!-- chunk 134 | 491 tokens | part 2/3 -->
Manual section: Resource > Appointment types > Financial handling > How to add an appointment type?

| **Field** | **Explanation** |
| --- | --- |
| Debtor Type | There are four types of debtors:   * Patient: Use this for declaration to the patient * Patient insurance: Used for people insured in the Netherlands or abroad or health insurers to whom you can submit claims directly. * Referrer organization: use this for mutual services where the invoice goes to, for example, another healthcare provider or a company. * Secondary debtor: if an organization/company or the like pays for the patient.  **TIP:** This body must be created in organizations and registered on the patient information page under the heading Paying body. |
| Financial Stream | There are four types of financial streams:   * Activity (Puls): for other care or care declared by an agency (B2B).   + Permitted debtor types: Health insurance, Referring organization or Paying agency * Activity Flex: for uninsured care that is invoiced immediately after an appointment has been completed.   + Authorized debtor type: Patient. * Ontario Health Insurance Policy (Canada) |
| **Other Settings** | |
| Instructions | If specific instructions are required for an appointment type, for example that a patient must appear fasting, these can be entered here. The instructions can be added as variables to notification templates. |
| Questionnaires | Questionnaires can be sent to a patient as soon as an appointment is scheduled. Questionnaires must be configured in advance for this. See questionnaires for instructions. |
| Letter template | The standard letter template that is chosen when creating a letter for this appointment can be set here. Letter templates must be configured in advance for this. See Letter Templates for instructions. |
| Allow planning without resources | Check if an appointment can be scheduled without resources. See Planning without resources for further explanation. |

---

<!-- chunk 135 | 72 tokens | part 3/3 -->
Manual section: Resource > Appointment types > Financial handling > How to add an appointment type?

| **Field** | **Explanation** |
| --- | --- |
| Allow direct planning | Check if an appointment should be able to be scheduled immediately. See Plan immediately for further explanation. |

---

<!-- chunk 136 | 158 tokens | part 1/1 -->
Manual section: Resource > Appointment types > Appointment content

Click on + Examination at the bottom of the appointment screen to add content to your appointment type. A new screen opens:

1. Select a survey type. If desired, it is possible to add a waiting room for the relevant examination. A waiting room is always added for the first examination of the appointment.
2. Click on Save.
3. Add as many exams and waiting rooms as necessary to complete the appointment.
4. You must select one study as the primary study. The executor linked to the resource of this research will be used as an implementer in the DBC registration.

---

<!-- chunk 137 | 81 tokens | part 1/1 -->
Manual section: Resource > Appointment types > Appointment content > Standard referrer

It is possible to select a default referrer for an appointment type. If possible, this referrer is automatically selected when scheduling an appointment. This means that the user no longer has to do this while scheduling the appointment.

---

<!-- chunk 138 | 470 tokens | part 1/1 -->
Manual section: Resource > Appointment types > Appointment content > Levels of notification templates

There are three levels of notification templates, namely general / location-specific / Departments-specific. You can link a maximum of one general template, one location-specific template and one Departments-specific template per appointment type. When sending notifications, the most specific template is automatically chosen based on the location and Departments of the appointment.

The order of selection is as follows:

1. **Section-specific template**: A specific location and Departments has been filled in for this template. If a Departments-specific template has been set up for the Departments of the appointment, this template will be sent.
2. **Location-specific template**: A specific location but no Departments has been entered for this template. If no Departments-specific template has been set, a check is made to see whether a location-specific template is available.
3. **General template**: No specific location or Departments has been entered for this template. If there is no location-specific template, the general template is used.

**NB:** If none of these templates are set up, no confirmation or reminder will be sent.

*Example: The following confirmation templates have been set for appointment type 'First consultation': 1. Confirmation Amsterdam - Cardiology; 2.. Confirmation Utrecht.*

*If an appointment for Amsterdam - Cardiology is scheduled, the Departments-specific template for Amsterdam Cardiology is used. If an appointment for Utrecht - Dermatology is scheduled, the location-specific template is used. No confirmation will be sent for an appointment in Rotterdam because no general template has been set.*

**NB:** Always select a general template for the appointment types to ensure that a confirmation or reminder can always be sent.

---

<!-- chunk 139 | 83 tokens | part 1/1 -->
Manual section: Resource > Appointment types > Appointment content > Planning without resources

When you have Planning without resources checked, it becomes possible for this appointment type to schedule an appointment without a resource having been selected for this. However, starting a survey by a user always requires a resource.

---

<!-- chunk 140 | 209 tokens | part 1/1 -->
Manual section: Resource > Appointment types > Appointment content > Direct Planning

The option Direct Planning makes it possible to schedule an appointment of the relevant appointment type with one click. If you have selected at least one appointment type for this, there will be an instant scheduling icon visible on the patient page and in the right sidebar of the patient file. When the user clicks this button, the appointment is scheduled for the current date and time.

In the event that a resource can be linked to the first investigation of the appointment, that specific investigation will open immediately. If this is not the case, the appointment opens as a whole.

If you have selected multiple appointment types for instant scheduling, after clicking the instant scheduling icon first choose the desired appointment type.

---

<!-- chunk 141 | 231 tokens | part 1/1 -->
Manual section: Resource > Reason for change

MedicalPortal offers the option to specify a reason for change when canceling or moving an appointment. Reasons for cancellations can also be declared financially invoiceable. If no reasons have been set for canceling or rescheduling an appointment, you will not be prompted for a reason in that process.

1. Go to Maintenance → Agenda - Edit Reasons
2. Click at the top right + Reason
3. Enter the description of the reason
4. Select when the reason should appear in the 'Type' field
5. You can link a registration code to the reason with the button + Registration code under the heading Finances. This heading is only visible if the 'Cancel appointment' type has been chosen.

End users will see the registered reason for canceling or moving an appointment on the page of the relevant appointment.

An overview of all registered reasons for changes can be shown in the Dashboard.

---

<!-- chunk 142 | 113 tokens | part 1/1 -->
Manual section: Resource > Reason for coming

MedicalPortal offers the option to specify a reason for coming when planning or changing an appointment. The user can choose from one of the reasons set for the specialty of the appointment or type a reason themselves. If no active reasons for coming have been set for the specialty of the appointment, the user only has the option to type a reason themselves. The reasons for arrival can be set as follows:

---

<!-- chunk 143 | 64 tokens | part 1/1 -->
Manual section: Resource > Reason for coming > How to add a reason for coming?

1. Go to Maintenance → Agenda - Reason for coming
2. Click at the top right + Reason
3. Enter the description of the reason
4. Select the specialty for the reason
5. Click on Save

---

<!-- chunk 144 | 172 tokens | part 1/1 -->
Manual section: Resource > Resources & Resourceweergaven

Calendar management is split into Resources and Resource views. In Resource views, you select which resources should be visible in the calendar. It is also possible to create a resource view of multiple resources together, for example for a Departments overview where all resources for a specific Departments are visible in one agenda.

*Example: Doctor Hans works in the clinic. There is a resource 'Doctor Hans'. This resource is located in the resource views 'Agenda Hans' and 'Departments overview'. All appointments where 'Doctor Hans' is selected as the resource are visible in the 'Agenda Hans' and 'Departments overview'.*

---

<!-- chunk 145 | 158 tokens | part 1/2 -->
Manual section: Resource > Resources & Resourceweergaven > Resources

Resources are divided into three types: agenda, room and bed. A agenda is

for example, the agenda of a specific doctor or group of doctors. A room can be used

to track the availability of a specific room (or device). A bed is

related to a room and can be used for recording.

Two resources can be selected per examination in an appointment: a resource and

a room. This allows you to keep track of doctor and room availability. For the

recordings, a bed can be selected.

**NB:** Beds are part of the Recording module, this module may not be available to you.

---

<!-- chunk 146 | 433 tokens | part 2/2 -->
Manual section: Resource > Resources & Resourceweergaven > Resources

1. Go to Maintenance → Agenda - Resources and click on + Agenda, + Room of + Bed top right
2. Enter the following information:
   1. Name
   2. Location
   3. Department
   4. Specialty
   5. Start and end date: From the start date, the resource can be used in appointments or recordings. If you enter an end date, the resource will be archived from that date.
   6. Cost Center: Cost Centers can be used to allocate healthcare costs and revenues to specific Departments or divisions within a Department. If this is not completed, the care will be invoiced to the Departments Cost Center.
   7. Cost Bearer: Cost objects represent units such as projects and are used to more accurately allocate costs and revenues. If this is not completed, the care will be invoiced to the Departments Cost Center.
3. Are you adding a agenda? Please also fill in the following fields:
   1. Resource type: a default resource type can be set for each Examination Types. This is used to determine which resources can be selected for this study. (For example resource type 'Specialist')
   2. Performer: Select which practitioner is responsible for this agenda. This field is mandatory for resources of type medical specialist and nurse specialist. The AGB code of the linked executor is used in the financial settlement of agreements where this executor is used.
   3. Shared resource: Select this check box if it concerns a resource from which multiple people work. If selected, no warning will be shown during appointment scheduling if the resource is busy at the same time.
4. Are you adding a bed? Please also fill in the following fields:
   1. Type
   2. Room
5. Click on Save

---

<!-- chunk 147 | 173 tokens | part 1/1 -->
Manual section: Resource > Resources & Resourceweergaven > Resources > Add resource type

In MedicalPortal you can determine which resource types are available for your clinic. This ensures that only relevant resource types are shown and unnecessary options are not visible.

1. Go to Maintenance → Agenda - Resources
2. Hover your mouse over the Resource Type column name: a will appear pencil icon
3. Click on the pencil icon to open the pop-up with the list of already selected resource types.
4. Click on + Resource type
5. Select a new resource type to add from one of the possible options
6. Click Save

A resource type can only be deleted if no resources of this type have yet been added.

---

<!-- chunk 148 | 157 tokens | part 1/1 -->
Manual section: Resource > Resources & Resourceweergaven > Resources > Add bed type

In MedicalPortal you can determine which bed types are available in your clinic. This prevents unnecessary bed types from being displayed if they are not available.

1. Go to Maintenance → Agenda - Resources
2. Navigate to the 'Bed' tab
3. Move your mouse over the column name Bed type: a will appear pencil icon
4. Click on the pencil icon to open a pop-up with the list of already selected bed types.
5. Click on + Type
6. Select a new bed type to add
7. Click Save

A bed type can only be removed if no beds of this type have yet been added.

---

<!-- chunk 149 | 287 tokens | part 1/1 -->
Manual section: Resource > Resources & Resourceweergaven > Resource views

In resource views select which resources should be visible in the calendar. Also it is

possible to create a resource view of multiple resources together, for example

for a Departments overview with all resources for a specific Departments in one agenda

are visible. For each resource view, you can select the appointment type or survey type level

select. Appointment type level resource views show the entire appointment in the calendar

and resource views. Resource views at the exam level show the individual exams within an appointment in the calendar.

1. Go to Maintenance → Agenda - Resource views
2. Click on + Resource view display
3. Enter the following information:
   1. Name
   2. Location
   3. Department
   4. Resource: select the resource(s) that should be visible in this view.
   5. Level
      1. Appointment type: All appointments in which the selected resource(s) appear in at least one study are displayed in this resource view.
      2. Examination Type: All examinations containing the selected resource(s) will be displayed in this resource view.

---

<!-- chunk 150 | 74 tokens | part 1/1 -->
Manual section: Resource > Roosters

To make planning appointments easier, it is possible to work with schedules. A day or part of a day is divided with appointments in a schedule template. These can then be applied to different resources. The applied schedules are visible in the agenda as drafts.

---

<!-- chunk 151 | 443 tokens | part 1/1 -->
Manual section: Resource > Roosters > Create schedule template

1. Go to Maintenance → Agenda - Schedules
2. Click the button + Template top right.
3. Enter the name, locations, Department, description and start and end dates.
4. Click on Save
5. Click on + New appointment: a pop-up will open for adding an appointment to the template (see Image Add appointment to schedule)
6. Enter the start time and appointment type: the examinations will become visible
7. If necessary, you can adjust the duration and resource type per survey. These changes only apply to this schedule. Changing the resource type is only possible if the 'Allow standard resource type only' checkbox is unchecked for this Examination Types.
8. Enter the resource per study: if you create a schedule that can be used for multiple resources, we recommend leaving the resources empty. These can be filled in when applying the schedule.
9. Click on Save + New to immediately add another appointment type to this schedule or click Save if you do not want to add any other appointments to the schedule.

*Image - Add appointment to schedule*

10. Check the schedule in the list or graphical view.
11. If desired, an appointment in the schedule can be changed, cloned or deleted. When cloning, the pop-up opens to add a new appointment with the same appointment type, duration, resource type and resource.
12. It is possible to change the resource with a bulk change for multiple appointments at the same time.
   1. Click on + Bulk change: a pop-up will open with a list of all studies
   2. Select the desired studies
   3. Click on Change resource
   4. Select the desired resource
   5. Click on Save
13. Click on Save when the grid is complete

Image - Screen with the overview of the schedule template

---

<!-- chunk 152 | 66 tokens | part 1/1 -->
Manual section: Resource > Notification templates

Notification templates are templates that can be used as an appointment confirmation, appointment reminder, overview or as a recipe. It is possible to use patient or appointment data in the templates using variables.

---

<!-- chunk 153 | 502 tokens | part 1/2 -->
Manual section: Resource > Notification templates > New notification template

1. Go to Maintenance → Agenda - Notification templates.
2. Click on + Template in the top right corner
3. Fill one *name* in
4. Select one *category*
5. Select one *e-mail trigger*
   1. With the *e-mail trigger* you can indicate whether this template should be sent via a secure email. For this to be successful, you must ensure that a secure mail service is set up Maintenance → Core - Communication Settings. How exactly you can set this is further explained in the chapter Communication Settings.
6. Select one *type template* (Confirmation/Reminder/Prescription/Overview)
   1. Confirmation: Confirmations are sent automatically once the appointment has been scheduled and can also be sent manually via the appointment page.
   2. Reminder: Reminders are sent a certain number of days before the appointment.
      1. If you choose this option, the field '*Days between reminder and appointment*'. In this field you can indicate how many days there should be between the reminder and the appointment. If the appointment is scheduled within this period, the reminder will not be sent.
   3. Overview: It is possible to create one template with the overview type. Make sure that it contains at least the variable 'Appointments overview'. This makes it possible to email or print an overview of all future appointments to the patient via the appointments page.
7. Select one *reporttype* (Email, Print, SMS)
   1. Email: This option is available for both confirmations and reminders.
   2. Print: This option is available for the confirmations and overview. You can print these messages to physically give to a patient or to send them.
   3. SMS: This option is only available for reminders.
8. Choose a location and Department.
9. Fill the template with text and variables: The variables contain patient or appointment specific information (for example 'patient display name' or 'appointment date').
10. Click on Save

**NB:**

---

<!-- chunk 154 | 77 tokens | part 2/2 -->
Manual section: Resource > Notification templates > New notification template

* Notification templates can only be used if they are linked to a appointment type or a series.
* When sending appointment reminders by SMS: ensure there are sufficient (automatic replenishment) of credits on your Spryng account.

---

<!-- chunk 155 | 370 tokens | part 1/2 -->
Manual section: Core > Contact book

You can register people in the contact book. You can also save contacts here who are not practitioners, so that you can easily find their contact details MedicalPortal. You can also register internal and external practitioners. For example, external practitioners can be selected as a patient's referrer. Internal practitioners can, for example, be assigned as executors on a resource or as the main practitioner of a patient.

* Go to Maintenance → Core - Contact Book
* Click at the top right + Contact
* Fill in the personal and contact details
  + E-mail address: this e-mail address is used to send letters
* Indicate whether the contact is a 'Practitioner'.

You can link the contact to one or more organizations via Work Relations.

* Click on + Add to add a working relationship
* Fill in the following fields:
  + Type of relationship: Choose internal if the contact works within your own organization, such as a doctor from the healthcare institution.
  + Start date
  + End date: if the working relationship ends, contact remains MedicalPortal visible for administrative purposes (e.g. financial settlement), but the contact can no longer be found from other parts of MedicalPortal and so this contact can no longer be used.
  + Email address: This is used for administrative purposes only. Used for sending emails MedicalPortal the contact's email address.

Is the contact a practitioner? Then you also fill in the following fields:

---

<!-- chunk 156 | 200 tokens | part 2/2 -->
Manual section: Core > Contact book

* + User: only applicable to an internal working relationship.
  + Organization: not applicable to an internal working relationship.
  + Practitioner type: the position of the practitioner (e.g. general practitioner)
  + Specialty
  + OHIP Billing Number (Canada): unique identifier assigned to healthcare providers for billing purposes under the Ontario Health Insurance Plan (OHIP)
  + CPSO Number (Canada): unique identifier assigned to licensed medical professionals by the College of Physicians and Surgeons of Ontario to ensure their credentials and practice are recognized
  + Practitioner code (Srbjia): unique identifier assigned to healthcare professionals to regulate and track their medical practice and qualifications within the country
* Click on Save

---

<!-- chunk 157 | 104 tokens | part 1/1 -->
Manual section: Core > Organizations > Why register organizations?

Organizations are in MedicalPortal used as a recipient of correspondence or referrer of an appointment. In order to select an organization as a recipient of, for example, orders, prescriptions, letters or invoices or to register as a referrer of an appointment or pharmacy of a patient, it must be registered with Maintenance → Core - Organizations.

---

<!-- chunk 158 | 201 tokens | part 1/1 -->
Manual section: Core > Organizations > Why register organizations? > How to register organizations?

To add an organization:

1. Go to Maintenance → Core - Organizations
2. Click at the top right + Organization
3. The following fields are required when creating an organization
   1. Name
   2. Organization type

**NB:** Certain fields are required when adding an insurance company. In addition, you can add contracts for this specific insurance company. To do this, go to the heading 'Insurance company Maintenance’.

4. The following fields are optional:
   1. Debtor number: Here you add the debtor number that is used in your accounting.
   2. TAX ID: Here you add the TAX identification number of the organization.
   3. Standard Currency (Srbija): This is the standard currency that u want to use.

---

<!-- chunk 159 | 121 tokens | part 1/1 -->
Manual section: Core > Organizations > The Departments

Departments can be added to the organization. For example, a Radiology Departments of a hospital that has different correspondence data than the organization itself. Click + Department in the table at the bottom of the organization screen. To add a Department, only the 'Name' field is required. The departments created here are not  the Departments of your own organization. For example, no appointments or agendas can be added.

---

<!-- chunk 160 | 111 tokens | part 1/1 -->
Manual section: Core > Organizations > The Departments > Contract for the entire insurance company

There must be a contract for the insurance company at any point in time. This means that there must be a contract without a start date and a contract without an end date. This could be the same contract. This is automatically set up for you when you add a new insurance company. In addition, contracts cannot overlap within an insurance company.

---

<!-- chunk 161 | 161 tokens | part 1/1 -->
Manual section: Core > Locations

Locations are the (physical) location(s) of your healthcare institution.

*Example: Location West of Hospital A.*

Departments can be linked to locations that you have set up. Calendars and appointment types can then be created for these Departments (see chapter The Departments).

You can add a location as follows:

1. Go to Maintenance → Core - Locations
2. Click at the top right + Location
3. Enter the following information here:
   1. Name
   2. Phone number
   3. E-mail address: This email address should be the same email address as in the email settings
   4. Address/PO Box details
4. Click on Save

---

<!-- chunk 162 | 147 tokens | part 1/1 -->
Manual section: Core > Communication Settings

It's in MedicalPortal possible to send letters, prescriptions, appointment confirmations and appointment reminders, for example to other (external) healthcare providers or patients. Depending on various factors, the message can be sent securely or non-securely, using different methods. The available methods are determined on the Communication Settings page. You can find the page via Maintenance → Core - Communication Settings.

There are various options for secure and non-secure emailing MedicalPortal:

* Non-secure:
  + SMTP
* Secure:

---

<!-- chunk 163 | 189 tokens | part 1/1 -->
Manual section: Core > Communication Settings > SMTP

SMTP is an unsecured mail method based on email addresses. Set up SMTP as follows:

1. Click on + Add SMTP setting on the Communication Settings page.
2. Request the following information from your IT manager:
   1. Mail Sender
   2. Port
   3. Host
   4. Username
   5. Password
3. Click on Save.

When SMTP is set up on the Communication Settings page, three actions are possible:

* Press the pencil icon to change the SMTP details.
* Press the letter icon to test the email setting. You will receive a popup where you can enter your email address. Then when you click send and the setting is correct, you will receive a test message in your inbox.
* Press the trash icon to remove the SMTP setting.

---

<!-- chunk 164 | 184 tokens | part 1/1 -->
Manual section: Core > Specialties

A specialty is linked to a practitioner in the field working relationship. In addition, it is also used in other entities within MedicalPortal. For example, a specialty can be linked to the Departments, Examination Typess, or Resources.

Adding a specialty works as follows:

1. Go to Maintenance → Core - Specialty
2. Click at the top right + Specialty
3. Here you enter the following information:
   1. Specialty
      The Specialty in this list come from the specialty list of [woke up](https://www.vektis.nl/standaardisatie/codelijsten/COD016-VEKT).
   2. Custom code
      This code is visible to users.
   3. Administration code
      Used for financial administrative purposes.
4. Click on Save

---

<!-- chunk 165 | 275 tokens | part 1/1 -->
Manual section: Core > The Departments

A Departments is a (physical) Departments of a healthcare institution.

*Example: Cardiology Outpatient Clinic Departments of West location of Hospital A.*

A Department is always linked to a location, An specialty and a administration. Agendas, users and appointment types are linked to Department. Departments play a central role in MedicalPortal.

You can add a Departments as follows:

1. Go to Maintenance → Core - Departments
2. Click at the top right + Department
3. Enter the following information here:
   1. Name
   2. Location
   3. Specialty
   4. Type: An indoor Departments MedicalPortal can be outpatient, inpatient or both. By default, type 'Outpatient' is selected. Depending on the type you select, the relevant Departments will be displayed in certain 'Departments' filters MedicalPortal.
   5. Phone number
   6. Author Email: Emails are sent to patients from this email address. If you do not enter anything here, the email address set for the location will be used.
   7. Administration
   8. Cost Bearer
   9. Cost Center
4. Click on Save

---

<!-- chunk 166 | 69 tokens | part 1/1 -->
Manual section: Core > Tenant Info

On the tenant info page you can change general maintenance that apply to your entire organization. You can find this page as follows: Maintenance → Core - Tenant Info. The information is divided into three sections, each described separately.

---

<!-- chunk 167 | 108 tokens | part 1/1 -->
Manual section: Core > Tenant Info > Organization details

General information about your organization, such as name and telephone numbers. It is also possible to upload a logo here. This logo is used, among other things, on recipes. In addition, it is possible to select a default country. This country is automatically filled in as the country code for telephone and fax numbers when creating patients, contacts and organizations.

---

<!-- chunk 168 | 86 tokens | part 1/1 -->
Manual section: Core > Tenant Info > Address details

The address of your organization. If your organization has a different postal or billing address, you can indicate and fill in this.
**TIP:** Bee Maintenance -> Core -> Locations you can enter an address per location. Once filled, this address will be used when creating orders and recipes.

---

<!-- chunk 169 | 75 tokens | part 1/4 -->
Manual section: Core > Tenant Info > Other details

The fields in the other details section are displayed in different places MedicalPortal used. Below you will find an overview of all fields available on this page, which module they affect and an explanation of the effect.

*Table: Tenant Info Fields*

---

<!-- chunk 170 | 499 tokens | part 2/4 -->
Manual section: Core > Tenant Info > Other details

| **Field name** | **Module** | **Explanation** |
| --- | --- | --- |
| PSP key |  | Only filled by H4H |
| PID- check-identifier | Patient | URL for connecting a local device to check ID cards. This field is only filled in by H4H. |
| treatment relation duration medical personnel | Authorizations | The duration of the treatment relationship between medical users and patients. A value of -1 disables the functionality for registering reason for access. See Reason for inspection for setting reasons. |
| treatment relationship duration non medical personnel | Authorizations | The duration of the treatment relationship between non-medical users and patients. A value of -1 disables the functionality for registering reason for access. See Reason for inspection for setting reasons. |
| Patient name default ordering | Patient | The default order for constructing a patient's display name. This order is followed when creating a patient. This order can be adjusted later in the patient file. Choose from the following options here:   * INITIALS\_LAST\_NAME * INITIALS\_PARTNER\_NAME * INITIALS\_LAST\_NAME\_PARTNER\_NAME * INITIALS\_PARTNER\_NAME\_LAST NAME * FIRST\_NAME\_MIDDLE\_NAME\_LAST\_NAME |
| Lock time limit | Agenda | The duration of a draft's lock in minutes. When scheduling by schedule, a draft is locked for a certain period of time for other users. |
| Default planning flow | Agenda | The standard way of planning in your clinic. When planning from a work list or from a patient file, the planning module will open in this way. |
| Period setting for fast track batches | Finances | A general ledger export is created once per the period set here, containing all activity flex invoices that were created in that period. |
| Ledger export provider | Finances | Here you indicate your accounting program. This will adjust the layout of the general ledger export so that it matches the import layout of your accounting program. |

---

<!-- chunk 171 | 476 tokens | part 3/4 -->
Manual section: Core > Tenant Info > Other details

| **Field name** | **Module** | **Explanation** |
| --- | --- | --- |
| Show confidentiality warning on start | Authorizations | When opening MedicalPortal a popup is shown to inform the user that he is working with sensitive information. This is a requirement from the NEN. This popup can be enabled or disabled here. |
| Default letter send method | Correspondence | The standard way to send letters from MedicalPortal. This can be deviated from in step 2 when sending the letter. |
| Organization local code |  | Only filled by H4H |
| Plan horizon for online planning (in weeks) | Agenda | The number of weeks in which a patient can schedule their appointment. This is used for the 'Online planning' functionality, this functionality is still under development. |
| Plan term for online planning (in days) | Agenda | The number of days a patient has to complete their plan task. This is used for the 'Online planning' functionality, this functionality is still under development. |
| Diagnose thesaurus enabled | General | This field indicates whether the Thesaurus Diagnostics functionality is enabled on your environment. This is informational and cannot be edited. |
| Ksyos enabled | General | This field indicates whether the Ksyos functionality is enabled on your environment. This is informational and cannot be edited. |
| Relation service enabled | General | This field indicates whether the Service Relationship functionality is enabled on your environment. This is informational and cannot be edited. |
| Show date on letter item | Correspondence | With this field you can determine whether the dates of the examinations should be displayed in a letter or not. |
| Bed planning enabled | General | This field indicates whether the Bed Scheduling functionality is enabled in your environment. This is informational and cannot be edited. |

---

<!-- chunk 172 | 121 tokens | part 4/4 -->
Manual section: Core > Tenant Info > Other details

| **Field name** | **Module** | **Explanation** |
| --- | --- | --- |
| Outgoing referrals enabled | General | This field indicates whether the Outbound Referrals functionality is enabled on your environment. This is informational and cannot be edited. |
| Inventory management | General | This field indicates whether the Inventory management functionality is enabled on your environment. This is informational and cannot be edited. |

---

<!-- chunk 173 | 230 tokens | part 1/1 -->
Manual section: Core > Functions

A function concerns the function of the user. The Functions list may differ per healthcare institution.

*Example: Cardiologist, Center Assistant, Ultrasoundist*

A user can select a feature in my account and then receive free requests addressed to this feature. Creating a new function is as follows:

1. Go to Maintenance → Core - Functions
2. Click at the top right + Function
3. Enter the following information:
   1. Code: function code
   2. Name: the name of the function
4. Then click Save

The function is saved and visible in the table. It is possible to archive functions so that they are no longer selectable in MedicalPortal. This can be done with the archive icon which appears when the cursor hovers over the function. Activating an archived function works like archiving: The user clicks on the activate icon, which appears when the cursor hovers over the function again.

---

<!-- chunk 174 | 165 tokens | part 1/1 -->
Manual section: Very common configuration actions > Add new locations and Departments

1. Locations add
   1. Enter the correct information for the new location

If the desired administration already exists, you can skip step 2

2. Administrations add
   1. Fill in the correct details

If the desired Cost Bearer and Cost Center already exists, you can skip steps 3 and 4.

3. Cost Bearers add
   1. Fill in the correct details
4. Cost Centers add
   1. Fill in the correct details
5. Departments add
   1. Enter the correct location and specialty
   2. Select the type (inpatient or outpatient)
   3. Select the desired Cost Bearer and Cost Center. (optional)

---

<!-- chunk 175 | 266 tokens | part 1/1 -->
Manual section: Very common configuration actions > Add new specialist

1. Users
   1. Be the first to add a new user for the specialist.
   2. Fill in the correct details
   3. Select the function and authorization group.
2. Contact Book
   1. Create a contact for the new specialist.
   2. Add an internal working relationship to the contact
   3. Fill in the correct details.
   4. Select the user in the working relationship.
   5. Select 'Medical specialist' as the practitioner type.
   6. Enter the correct AGB code.
3. Resources
   1. Create a resource for each location and Department where the specialist works
   2. Fill in the correct details.
   3. Select the specialist resource type
   4. Select the desired location and Department
   5. Select the doctor as the executor
   6. Enter the correct start date and, if known, also the end date
4. Resource views
   1. Create new resource view for the new doctor
      1. Choose from a research or appointment view.
   2. Add the new resource to other relevant resources (for example, a Department overview)

---

<!-- chunk 176 | 231 tokens | part 1/1 -->
Manual section: Very common configuration actions > New nurse (shared agenda)

Some clinics do not use personal agendas for nurses but use a resource that is shared by all nurses.

1. Users
   1. First add a new user for the nurse

If a shared agenda for the nurse already exists, the nurse can use it. If not, follow steps 2 and 3.

2. Resources
   1. Put a new resource for the nurse group
   2. Fill in the correct details
   3. Select the nurse resource type
   4. Select the location and Department
   5. Leave the operator blank or choose a medical specialist who is always responsible for the care provided by this resource.
   6. Enter the correct start date
   7. Select the 'Shared calendar' checkbox.
3. Resource views
   1. Create new resource views for the new nurses
      1. Choose from a research or appointment view.
   2. Add the new resource to other relevant resources (for example, a Department overview)

---

<!-- chunk 177 | 214 tokens | part 1/1 -->
Manual section: Very common configuration actions > Specialist retired

1. Resource view to delete
   1. Start by removing the physician's resource views so that they are no longer visible in the calendar. There is no need to manually remove the doctor from shared resource views.
2. Resources archive
   1. Archive the physician resource by entering the correct end date. Once this date has passed, it will no longer be possible to select this resource when scheduling an appointment.
3. Working relationship archive
   1. Archive the doctor's internal working relationship in the contact book by entering the correct end date.
   2. If known, you can immediately add the new external working relationship.
4. Users archive
   1. Archive the user by changing the user's status from active to inactive. After this, the user can no longer log into the system

---

<!-- chunk 178 | 228 tokens | part 1/1 -->
Manual section: Very common configuration actions > Add new survey type

If the desired resource types already exist, you can skip step 1

1. Resourcetype add
   1. Select the correct resource type to add it

If the desired Finance code already exists, you can skip step 2

2. Registration codes add
   1. Enter the correct information
3. Examination Types add
   1. Fill in the correct details
   2. Select the correct (default) resource type
   3. Add the correct registration code(s).
4. Examination Segments add
   1. Fill in the correct fields
   2. Change segment content
      1. Add the desired OTP fields to the segment
5. Examination Forms add
   1. Fill in the correct fields
   2. Change form content
      1. Add the desired segments to the form
6. Examination Views add
   1. Select the correct Examination Type
   2. Change the examination view
      1. Select the correct forms or functionalities

---

<!-- chunk 179 | 297 tokens | part 1/1 -->
Manual section: Very common configuration actions > Add new appointment type

If the desired Examination Types already exists, you can skip step 1

1. Examination Types add
   1. Fill in the correct details
   2. Select the correct (default) resource type
   3. Add the correct registration code(s).

If the desired notification template already exists, you can skip step 2, the notification templates are not mandatory.

2. Notification Template to make
   1. Fill in the correct details.

If the desired letter template already exists, you can skip steps 3 and 4.

3. Letter Items add
   1. Fill in the correct details
4. Letter templates to make
   1. Fill in the correct details
   2. Select the desired letter items and variable.

If the desired questionnaires already exist, you can skip step 5

5. Questionnaires add
   1. Fill in the correct fields
   2. Select the desired forms
6. Appointment type add
   1. Fill in the correct details
   2. Select the desired examination type
   3. Select the desired letter templates
   4. Select the desired notification templates (optional)
   5. Select the desired package code (optional)
   6. Select the desired questionnaires (optional)

---

<!-- chunk 180 | 65 tokens | part 1/1 -->
Manual section: Very common configuration actions > Recurring promotions for the new year

Every year there are changes in prices and health insurance. These must be updated before the new year (before January 1) in MedicalPortal. See the required actions below.

---

<!-- chunk 181 | 115 tokens | part 1/1 -->
Manual section: Very common configuration actions > Recurring promotions for the new year > 1. Update health insurance in organizations

It is important that all information from health insurers is correct MedicalPortal stands. Changes in the organization of the health insurer (for example a changed name) can be changed at Maintenance → Core - Organizations. More information about this can be found in the Core chapter and then in the section organizations.

---

<!-- chunk 182 | 121 tokens | part 1/1 -->
Manual section: Very common configuration actions > Recurring promotions for the new year > 2. Redesign organization groups

It is possible that some labels and health insurers charge the same prices within the group. MedicalPortal offers the option to group these organizations into so-called Organization Groups. This may change every year and should therefore be updated MedicalPortal. You can find out how to change this in the chapter Maintenance → Finance - organization groups.

---

<!-- chunk 183 | 174 tokens | part 1/1 -->
Manual section: Very common configuration actions > Recurring promotions for the new year > 3. Update price matrix

Healthcare prices change every year. The price matrix is the place to register prices from organizations (health insurers, your own rate or the passer-by rate) per declaration code. Correct design of the price matrix ensures that the care is invoiced with the correct rate, invoice type and any discount or VAT percentage. This must be updated every year for the insured care with a new import with Import DBC system. To add prices for uninsured care, you must add this manually per declaration code. More information about this can be found in the chapter Finance - Price Matrix.

---

<!-- chunk 184 | 220 tokens | part 1/1 -->
Manual section: Very common configuration actions > Recurring promotions for the new year > Configure contracting for certain policies

1. Go to Maintenance → Finance → Price matrix
2. Click on Edit price matrix ✎ or add a line via + Price of in bulk:
3. Using the Package code field you can define a rule for the situation in which there is a deviating agreement with a certain policy compared to the contract with the health insurer.
   1. Bill directly to the patient: set the invoice type to On Paper.
   2. Invoicing the patient via Health Care Payment (Canada): set the invoice type to Health Care Payment
   3. Invoicing the patient via Proforma (SR): set the invoice type to Proforma

**NB**:

* The value of a package code must correspond to the data from the COV check.
* Presence/absence of contract per policy (package) must also be configured correctly Organizations.

---

