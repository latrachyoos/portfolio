<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form esegue l'override del metodo Dispose per pulire l'elenco dei componenti.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Richiesto da Progettazione Windows Form
    Private components As System.ComponentModel.IContainer

    'NOTA: la procedura che segue è richiesta da Progettazione Windows Form
    'Può essere modificata in Progettazione Windows Form.  
    'Non modificarla nell'editor del codice.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.btnfaqualcosa = New System.Windows.Forms.Button()
        Me.btnnazioni = New System.Windows.Forms.Button()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.cmbnazioni = New System.Windows.Forms.ComboBox()
        Me.btnclienti = New System.Windows.Forms.Button()
        Me.ListBox1 = New System.Windows.Forms.ListBox()
        Me.txtquery = New System.Windows.Forms.TextBox()
        Me.dgv = New System.Windows.Forms.DataGridView()
        Me.sendquery = New System.Windows.Forms.Button()
        Me.Button1 = New System.Windows.Forms.Button()
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.SuspendLayout()
        '
        'btnfaqualcosa
        '
        Me.btnfaqualcosa.Location = New System.Drawing.Point(12, 12)
        Me.btnfaqualcosa.Name = "btnfaqualcosa"
        Me.btnfaqualcosa.Size = New System.Drawing.Size(107, 75)
        Me.btnfaqualcosa.TabIndex = 0
        Me.btnfaqualcosa.Text = "schiacciami"
        Me.btnfaqualcosa.UseVisualStyleBackColor = True
        '
        'btnnazioni
        '
        Me.btnnazioni.Location = New System.Drawing.Point(12, 93)
        Me.btnnazioni.Name = "btnnazioni"
        Me.btnnazioni.Size = New System.Drawing.Size(107, 75)
        Me.btnnazioni.TabIndex = 1
        Me.btnnazioni.Text = "schiaccia anche me"
        Me.btnnazioni.UseVisualStyleBackColor = True
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(125, 93)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(74, 13)
        Me.Label1.TabIndex = 2
        Me.Label1.Text = "mostra nazioni"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(125, 23)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(104, 13)
        Me.Label2.TabIndex = 3
        Me.Label2.Text = "mostra nome società"
        '
        'cmbnazioni
        '
        Me.cmbnazioni.FormattingEnabled = True
        Me.cmbnazioni.Location = New System.Drawing.Point(12, 174)
        Me.cmbnazioni.Name = "cmbnazioni"
        Me.cmbnazioni.Size = New System.Drawing.Size(121, 21)
        Me.cmbnazioni.TabIndex = 4
        '
        'btnclienti
        '
        Me.btnclienti.Location = New System.Drawing.Point(125, 132)
        Me.btnclienti.Name = "btnclienti"
        Me.btnclienti.Size = New System.Drawing.Size(68, 36)
        Me.btnclienti.TabIndex = 5
        Me.btnclienti.Text = "e non mi schiacci"
        Me.btnclienti.UseVisualStyleBackColor = True
        '
        'ListBox1
        '
        Me.ListBox1.FormattingEnabled = True
        Me.ListBox1.Location = New System.Drawing.Point(235, 23)
        Me.ListBox1.Name = "ListBox1"
        Me.ListBox1.Size = New System.Drawing.Size(142, 277)
        Me.ListBox1.TabIndex = 6
        '
        'txtquery
        '
        Me.txtquery.Location = New System.Drawing.Point(843, 23)
        Me.txtquery.Multiline = True
        Me.txtquery.Name = "txtquery"
        Me.txtquery.Size = New System.Drawing.Size(383, 128)
        Me.txtquery.TabIndex = 7
        '
        'dgv
        '
        Me.dgv.AllowUserToAddRows = False
        Me.dgv.AllowUserToDeleteRows = False
        Me.dgv.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.AllCells
        Me.dgv.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.dgv.Location = New System.Drawing.Point(520, 187)
        Me.dgv.Name = "dgv"
        Me.dgv.ReadOnly = True
        Me.dgv.Size = New System.Drawing.Size(741, 580)
        Me.dgv.TabIndex = 8
        '
        'sendquery
        '
        Me.sendquery.Location = New System.Drawing.Point(579, 49)
        Me.sendquery.Name = "sendquery"
        Me.sendquery.Size = New System.Drawing.Size(175, 80)
        Me.sendquery.TabIndex = 9
        Me.sendquery.Text = "SEND"
        Me.sendquery.UseVisualStyleBackColor = True
        '
        'Button1
        '
        Me.Button1.Location = New System.Drawing.Point(386, 360)
        Me.Button1.Name = "Button1"
        Me.Button1.Size = New System.Drawing.Size(75, 23)
        Me.Button1.TabIndex = 10
        Me.Button1.Text = "Button1"
        Me.Button1.UseVisualStyleBackColor = True
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1409, 841)
        Me.Controls.Add(Me.Button1)
        Me.Controls.Add(Me.sendquery)
        Me.Controls.Add(Me.dgv)
        Me.Controls.Add(Me.txtquery)
        Me.Controls.Add(Me.ListBox1)
        Me.Controls.Add(Me.btnclienti)
        Me.Controls.Add(Me.cmbnazioni)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.btnnazioni)
        Me.Controls.Add(Me.btnfaqualcosa)
        Me.Name = "Form1"
        Me.Text = "Form1"
        CType(Me.dgv, System.ComponentModel.ISupportInitialize).EndInit()
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub
    Friend WithEvents btnfaqualcosa As System.Windows.Forms.Button
    Friend WithEvents btnnazioni As System.Windows.Forms.Button
    Friend WithEvents Label1 As System.Windows.Forms.Label
    Friend WithEvents Label2 As System.Windows.Forms.Label
    Friend WithEvents cmbnazioni As System.Windows.Forms.ComboBox
    Friend WithEvents btnclienti As System.Windows.Forms.Button
    Friend WithEvents ListBox1 As System.Windows.Forms.ListBox
    Friend WithEvents txtquery As System.Windows.Forms.TextBox
    Friend WithEvents dgv As System.Windows.Forms.DataGridView
    Friend WithEvents sendquery As System.Windows.Forms.Button
    Friend WithEvents Button1 As System.Windows.Forms.Button

End Class
